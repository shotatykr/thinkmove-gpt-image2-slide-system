#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 /path/to/thinkmove-design-system" >&2
  exit 1
fi

SOURCE_DIR="$(cd "$1" && pwd)"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for required in worldview/core.md worldview/voice.md theme/design.json theme/globals.css assets/logo.png; do
  if [ ! -f "$SOURCE_DIR/$required" ]; then
    echo "Missing upstream file: $SOURCE_DIR/$required" >&2
    exit 1
  fi
done

STAGE_DIR="$(mktemp -d)"
trap 'rm -rf "$STAGE_DIR"' EXIT

mkdir -p "$STAGE_DIR/brand/worldview" "$STAGE_DIR/brand/theme" "$STAGE_DIR/assets/references"
cp "$SOURCE_DIR/worldview/core.md" "$STAGE_DIR/brand/worldview/core.md"
cp "$SOURCE_DIR/worldview/voice.md" "$STAGE_DIR/brand/worldview/voice.md"
cp "$SOURCE_DIR/theme/design.json" "$STAGE_DIR/brand/theme/design.json"
cp "$SOURCE_DIR/theme/globals.css" "$STAGE_DIR/brand/theme/globals.css"
cp -R "$SOURCE_DIR/assets/." "$STAGE_DIR/assets/references/"

rm -f "$STAGE_DIR/assets/references/icons/_contact-sheet.html"
rm -f "$STAGE_DIR/assets/references/diagrams/_contact-sheet.html"
if [ -f "$STAGE_DIR/assets/references/README.md" ]; then
  mv "$STAGE_DIR/assets/references/README.md" "$STAGE_DIR/assets/references/SOURCE_MANIFEST.md"
fi

rsync -a --delete "$STAGE_DIR/brand/" "$ROOT_DIR/brand/"
rsync -a --delete "$STAGE_DIR/assets/references/" "$ROOT_DIR/assets/references/"

echo "Synced brand and reference assets. Review with git diff before committing."
