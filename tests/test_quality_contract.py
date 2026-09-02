from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validate_manifest = load_module("validate_manifest", ROOT / "scripts" / "validate_manifest.py")
qa_images = load_module("qa_images", ROOT / "scripts" / "qa_images.py")


class QualityContractTest(unittest.TestCase):
    def setUp(self) -> None:
        self.example_path = ROOT / "templates" / "deck-manifest.example.json"
        self.example = json.loads(self.example_path.read_text(encoding="utf-8"))

    def write_manifest(self, folder: Path, manifest: dict) -> Path:
        path = folder / "manifest.json"
        path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
        return path

    def approve_example(self, folder: Path) -> tuple[dict, Path]:
        manifest = copy.deepcopy(self.example)
        manifest["versions"]["system_commit"] = "1234567"
        slide = manifest["slides"][0]
        slide["status"] = "approved"
        slide["selected_attempt"] = 1
        slide["attempts"] = [
            {
                "number": 1,
                "prompt_file": "prompts/01.txt",
                "references": [slide["anchor"]],
                "output_file": "01-cover.png",
                "result": "accepted",
                "rejection_reasons": [],
                "copy_change": None,
            }
        ]
        slide["qa"] = {
            "hard_failures": [],
            "scores": {
                "source_fidelity": 30,
                "readability": 18,
                "visual_family": 18,
                "layout_spacing": 14,
                "narrative_role": 10,
                "brand_handling": 5,
            },
            "human_approved": True,
            "approved_by": "reviewer",
        }
        manifest["release"] = {
            "status": "approved",
            "approved_by": "reviewer",
            "approved_at": "2026-09-02T10:00:00+09:00",
        }
        return manifest, self.write_manifest(folder, manifest)

    def test_example_is_valid_draft(self) -> None:
        errors, warnings = validate_manifest.validate(self.example_path)
        self.assertEqual(errors, [])
        self.assertTrue(any("sha256" in warning for warning in warnings))

    def test_contact_sheet_is_rejected_as_model_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest = copy.deepcopy(self.example)
            manifest["slides"][0]["anchor"] = "contact-sheet.png"
            path = self.write_manifest(Path(temp), manifest)
            errors, _ = validate_manifest.validate(path)
        self.assertTrue(any("contact sheet" in error for error in errors))

    def test_release_requires_human_gate(self) -> None:
        errors, _ = validate_manifest.validate(self.example_path, release=True)
        self.assertTrue(any("human approval" in error for error in errors))
        self.assertTrue(any("status must be approved" in error for error in errors))

    def test_version_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest = copy.deepcopy(self.example)
            manifest["versions"]["prompt"] = "9.9.9"
            path = self.write_manifest(Path(temp), manifest)
            errors, _ = validate_manifest.validate(path)
        self.assertTrue(any("system/versions.json" in error for error in errors))

    def test_approved_image_passes_file_qa(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            manifest, manifest_path = self.approve_example(folder)
            final_dir = folder / "final"
            final_dir.mkdir()
            Image.new("RGB", (1536, 864), "white").save(final_dir / "01-cover.png")
            release_errors, _ = validate_manifest.validate(manifest_path, release=True)
            report = qa_images.inspect(manifest_path, final_dir)
        self.assertEqual(release_errors, [])
        self.assertTrue(report["passed"])

    def test_wrong_image_size_fails_file_qa(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            _, manifest_path = self.approve_example(folder)
            final_dir = folder / "final"
            final_dir.mkdir()
            Image.new("RGB", (1024, 1024), "white").save(final_dir / "01-cover.png")
            report = qa_images.inspect(manifest_path, final_dir)
        self.assertFalse(report["passed"])
        self.assertTrue(any("expected 1536x864" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
