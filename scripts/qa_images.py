#!/usr/bin/env python3
"""Run deterministic file-level QA on final GPT-image2 slide images."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image


ALLOWED_SUFFIXES = {".png", ".jpg", ".jpeg"}


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def selected_filename(slide: dict[str, Any]) -> str | None:
    selected = slide.get("selected_attempt")
    for attempt in slide.get("attempts", []):
        if attempt.get("number") == selected:
            return Path(attempt["output_file"]).name
    return None


def inspect(manifest_path: Path, final_dir: Path) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    expected_width = manifest["generation"]["width"]
    expected_height = manifest["generation"]["height"]
    errors: list[str] = []
    images: list[dict[str, Any]] = []
    expected_names: list[str] = []

    for slide in manifest["slides"]:
        name = selected_filename(slide)
        if name is None:
            errors.append(f"slide {slide['index']}: no selected accepted attempt")
            continue
        expected_names.append(name)
        path = final_dir / name
        record: dict[str, Any] = {"slide": slide["index"], "file": name, "passed": False}
        if not path.exists():
            errors.append(f"slide {slide['index']}: missing final image {name}")
            images.append(record)
            continue
        if path.suffix.lower() not in ALLOWED_SUFFIXES:
            errors.append(f"slide {slide['index']}: unsupported image type {path.suffix}")
            images.append(record)
            continue
        try:
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                width, height = image.size
                mode = image.mode
        except Exception as exc:  # Pillow exposes format-specific errors.
            errors.append(f"slide {slide['index']}: unreadable image {name}: {exc}")
            images.append(record)
            continue

        record.update({"width": width, "height": height, "mode": mode})
        if (width, height) != (expected_width, expected_height):
            errors.append(
                f"slide {slide['index']}: expected {expected_width}x{expected_height}, got {width}x{height}"
            )
        if mode not in {"RGB", "RGBA"}:
            errors.append(f"slide {slide['index']}: expected RGB/RGBA, got {mode}")
        record["passed"] = not any(error.startswith(f"slide {slide['index']}:") for error in errors)
        images.append(record)

    actual_names = sorted(
        path.name for path in final_dir.iterdir() if path.is_file() and path.suffix.lower() in ALLOWED_SUFFIXES
    ) if final_dir.exists() else []
    extras = sorted(set(actual_names) - set(expected_names))
    if extras:
        errors.append(f"unexpected images in final/: {', '.join(extras)}")
    if len(expected_names) != len(manifest["slides"]):
        errors.append("not every slide has a selected final image")

    return {
        "passed": not errors,
        "manifest": str(manifest_path),
        "final_dir": str(final_dir),
        "errors": errors,
        "images": images,
        "manual_checks_required": [
            "visible Japanese, names, numbers, units, and periods match source",
            "claim and visual meaning match",
            "no invented facts, UI, logos, signatures, or watermarks",
            "no clipping, overlap, tangency, or unsafe lower-edge decoration",
            "contact sheet has one visual family and clear narrative rhythm",
            "logo and person are generated likenesses, not pixel-identical official assets",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("final_dir", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    report = inspect(args.manifest, args.final_dir)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
