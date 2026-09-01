#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

jq empty brand/theme/design.json upstream.json system.json
find assets/references -name '*.svg' -print0 | xargs -0 -n1 xmllint --noout

for required in AGENTS.md README.md system/production-guide.md system/qa-checklist.md prompts/base-slide.md assets/references/logo.png; do
  test -e "$required" || { echo "Missing required path: $required" >&2; exit 1; }
done

if find . -path './.git' -prune -o -name '*.html' -print | grep -q .; then
  echo "HTML files are not allowed in the GPT-image-2-only repository." >&2
  exit 1
fi

echo "Repository validation passed."
