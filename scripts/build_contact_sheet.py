#!/usr/bin/env python3
"""Build a contact sheet without altering the source slide images."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Directory containing final PNG/JPEG slides")
    parser.add_argument("output", type=Path, help="Output contact-sheet PNG")
    args = parser.parse_args()

    slides = sorted([*args.input.glob("*.png"), *args.input.glob("*.jpg"), *args.input.glob("*.jpeg")])
    if not slides:
        raise SystemExit(f"No slide images found in {args.input}")

    thumb_w, thumb_h = 640, 360
    gap, label_h, margin = 32, 48, 48
    cols = 2
    rows = (len(slides) + cols - 1) // cols
    sheet = Image.new("RGB", (margin * 2 + cols * thumb_w + gap, margin * 2 + rows * (thumb_h + label_h + gap)), "#fafbfc")
    draw = ImageDraw.Draw(sheet)

    for index, slide_path in enumerate(slides):
        row, col = divmod(index, cols)
        x = margin + col * (thumb_w + gap)
        y = margin + row * (thumb_h + label_h + gap)
        image = Image.open(slide_path).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (thumb_w, thumb_h), "white")
        canvas.paste(image, ((thumb_w - image.width) // 2, (thumb_h - image.height) // 2))
        sheet.paste(canvas, (x, y))
        draw.rounded_rectangle((x, y, x + thumb_w, y + thumb_h), radius=12, outline="#d8e0e8", width=2)
        draw.text((x, y + thumb_h + 12), slide_path.stem, fill="#0a1628", font=font(22))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output)
    print(f"built {args.output} from {len(slides)} slides")


if __name__ == "__main__":
    main()
