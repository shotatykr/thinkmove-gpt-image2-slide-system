#!/usr/bin/env python3
"""Validate a deck manifest before generation or release."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "deck.schema.json"
VERSIONS_PATH = ROOT / "system" / "versions.json"
UPSTREAM_PATH = ROOT / "upstream.json"
SCORE_KEYS = (
    "source_fidelity",
    "readability",
    "visual_family",
    "layout_spacing",
    "narrative_role",
    "brand_handling",
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def semantic_errors(manifest: dict[str, Any], release: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    slides = manifest.get("slides", [])
    sources = manifest.get("sources", [])
    generation = manifest.get("generation", {})
    manifest_versions = manifest.get("versions", {})
    declared_versions = load_json(VERSIONS_PATH)
    upstream = load_json(UPSTREAM_PATH)

    for key in ("skill", "prompt"):
        if manifest_versions.get(key) != declared_versions.get(key):
            errors.append(
                f"versions.{key} must match system/versions.json: {declared_versions.get(key)!r}"
            )
    if manifest_versions.get("design_commit") != upstream.get("commit"):
        errors.append("versions.design_commit must match upstream.json commit")

    indices = [slide.get("index") for slide in slides]
    if indices != list(range(1, len(slides) + 1)):
        errors.append("slides must be ordered and contiguous from index 1")

    source_ids = [source.get("id") for source in sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("source ids must be unique")
    for source in sources:
        if not source.get("verified"):
            errors.append(f"source {source.get('id')!r} is not verified")
        if source.get("sha256") is None:
            warnings.append(f"source {source.get('id')!r} has no sha256")

    width = generation.get("width", 0)
    height = generation.get("height", 1)
    if height and abs((width / height) - (16 / 9)) > 0.002:
        errors.append(f"generation size must be 16:9, got {width}x{height}")

    output_files: list[str] = []
    for slide in slides:
        prefix = f"slide {slide.get('index')}"
        if slide.get("title") not in slide.get("visible_japanese", []):
            errors.append(f"{prefix}: title must be included in visible_japanese")
        if "contact-sheet" in str(slide.get("anchor", "")).lower():
            errors.append(f"{prefix}: contact sheet cannot be used as an anchor")

        unknown_evidence = sorted(set(slide.get("evidence", [])) - set(source_ids))
        if unknown_evidence:
            errors.append(f"{prefix}: unknown evidence ids: {', '.join(unknown_evidence)}")

        attempts = slide.get("attempts", [])
        attempt_numbers = [attempt.get("number") for attempt in attempts]
        if attempt_numbers != list(range(1, len(attempts) + 1)):
            errors.append(f"{prefix}: attempts must be ordered and contiguous from 1")

        for attempt in attempts:
            output_files.append(attempt.get("output_file", ""))
            result = attempt.get("result")
            reasons = attempt.get("rejection_reasons", [])
            if result == "rejected" and not reasons:
                errors.append(f"{prefix} attempt {attempt.get('number')}: rejected attempts need a reason")
            if result == "accepted" and reasons:
                errors.append(f"{prefix} attempt {attempt.get('number')}: accepted attempts cannot have rejection reasons")
            if slide.get("copy_locked") and attempt.get("copy_change") is not None:
                errors.append(f"{prefix} attempt {attempt.get('number')}: copy_locked text cannot change")
            if any("contact-sheet" in ref.lower() for ref in attempt.get("references", [])):
                errors.append(f"{prefix} attempt {attempt.get('number')}: contact sheet cannot be a model input")

        selected = slide.get("selected_attempt")
        if selected is not None:
            matching = [attempt for attempt in attempts if attempt.get("number") == selected]
            if not matching or matching[0].get("result") != "accepted":
                errors.append(f"{prefix}: selected_attempt must point to an accepted attempt")

        if slide.get("status") == "blocked" and len(attempts) < generation.get("max_attempts", 3):
            warnings.append(f"{prefix}: blocked before the retry limit")

        if release:
            qa = slide.get("qa", {})
            scores = qa.get("scores", {})
            score_total = sum(scores.get(key, 0) for key in SCORE_KEYS)
            if slide.get("status") != "approved":
                errors.append(f"{prefix}: status must be approved for release")
            if selected is None:
                errors.append(f"{prefix}: selected_attempt is required for release")
            if qa.get("hard_failures"):
                errors.append(f"{prefix}: hard failures remain")
            if score_total < 90:
                errors.append(f"{prefix}: QA score is {score_total}, minimum is 90")
            if not qa.get("human_approved") or not qa.get("approved_by"):
                errors.append(f"{prefix}: human approval and approver are required")

    nonempty_outputs = [name for name in output_files if name]
    if len(nonempty_outputs) != len(set(nonempty_outputs)):
        errors.append("attempt output_file values must be unique")

    if manifest_versions.get("system_commit", "").startswith("REPLACE_"):
        warnings.append("versions.system_commit is still a placeholder")
        if release:
            errors.append("versions.system_commit must be pinned for release")

    if release:
        release_data = manifest.get("release", {})
        if release_data.get("status") != "approved":
            errors.append("release.status must be approved")
        if not release_data.get("approved_by") or not release_data.get("approved_at"):
            errors.append("release approver and approval timestamp are required")

    return errors, warnings


def validate(path: Path, release: bool = False) -> tuple[list[str], list[str]]:
    manifest = load_json(path)
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.absolute_path))
    ]
    semantic, warnings = semantic_errors(manifest, release)
    return schema_errors + semantic, warnings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--release", action="store_true", help="Require all release gates")
    args = parser.parse_args()

    errors, warnings = validate(args.manifest, args.release)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    stage = "release" if args.release else "draft"
    print(f"Manifest validation passed ({stage}): {args.manifest}")


if __name__ == "__main__":
    main()
