#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 /path/to/thinkmove-design-system" >&2
  exit 1
fi

SOURCE_DIR="$(cd "$1" && pwd)"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for required in worldview/core.md worldview/voice.md theme/design.json assets/logo.png assets/profile/toyokura-shota.jpg; do
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
cp "$SOURCE_DIR/assets/logo.png" "$STAGE_DIR/assets/references/logo.png"
cp -R "$SOURCE_DIR/assets/profile" "$STAGE_DIR/assets/references/profile"
cp -R "$SOURCE_DIR/assets/logos" "$STAGE_DIR/assets/references/logos"
cp -R "$SOURCE_DIR/assets/manga" "$STAGE_DIR/assets/references/manga"

sed -i.bak \
  -e 's|\[`theme/globals.css`\](../theme/globals.css) ／ \[`theme/design.json`\](../theme/design.json)|[`DESIGN.md`](../../DESIGN.md) と [`theme/design.json`](../theme/design.json)|g' \
  -e 's|\[`theme/globals.css`\](../theme/globals.css) と \[`theme/design.json`\](../theme/design.json)|[`DESIGN.md`](../../DESIGN.md) と [`theme/design.json`](../theme/design.json)|g' \
  "$STAGE_DIR/brand/worldview/core.md"
rm -f "$STAGE_DIR/brand/worldview/core.md.bak"

sed -i.bak -E \
  's#^  "\$description": ".*",$#  "$description": "ThinkMove visual token snapshot for GPT-image2 prompt reference. DESIGN.md is the human-readable authority.",#' \
  "$STAGE_DIR/brand/theme/design.json"
rm -f "$STAGE_DIR/brand/theme/design.json.bak"

rsync -a --delete "$STAGE_DIR/brand/" "$ROOT_DIR/brand/"
rsync -a --delete "$STAGE_DIR/assets/references/" "$ROOT_DIR/assets/references/"

echo "Synced brand and reference assets. Review with git diff before committing."
