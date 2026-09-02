#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TM_PYTHON="${TM_PYTHON:-python3}"
cd "$ROOT_DIR"

jq empty brand/theme/design.json upstream.json system/versions.json schemas/deck.schema.json templates/deck-manifest.example.json evals/cases.json

for required in \
  AGENTS.md \
  DESIGN.md \
  STYLE.md \
  README.md \
  .agents/skills/thinkmove-gpt-image2-slide/SKILL.md \
  .agents/skills/thinkmove-gpt-image2-slide/agents/openai.yaml \
  system/production-guide.md \
  system/manifest-contract.md \
  system/versions.json \
  system/qa-checklist.md \
  schemas/deck.schema.json \
  templates/deck-manifest.example.json \
  evals/cases.json \
  evals/rubric.md \
  prompts/base-slide.md \
  scripts/validate_manifest.py \
  scripts/qa_images.py \
  assets/references/logo.png; do
  test -e "$required" || { echo "Missing required path: $required" >&2; exit 1; }
done

if find . -path './.git' -prune -o -name '*.html' -print | grep -q .; then
  echo "HTML files are not allowed in the GPT-image-2-only repository." >&2
  exit 1
fi

if find assets/references -type f \( -name '*.svg' -o -name '*.html' \) | grep -q .; then
  echo "Reference assets must be directly usable raster inputs, not SVG or HTML." >&2
  exit 1
fi

"$TM_PYTHON" scripts/validate_manifest.py templates/deck-manifest.example.json
"$TM_PYTHON" -m unittest discover -s tests -p 'test_*.py'

echo "Repository validation passed."
