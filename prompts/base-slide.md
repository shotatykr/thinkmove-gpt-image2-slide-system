# Base Slide Prompt

```text
Create one finished 16:9 Japanese presentation slide as a single raster image.

PAGE ROLE
[cover / question / evidence / process / case / decision / closing]

CLAIM
[このページで残す結論]

VISIBLE JAPANESE
- Main title: 「[短い見出し]」
- Supporting labels: 「[短い要素]」「[短い要素]」「[短い要素]」
- Copy lock: [locked / may shorten after human approval]

EVIDENCE
[sourceで確認済みの数字・事実・引用。なければ作らない]

COMPOSITION
[視線の流れ、人物、図解、カード、余白、情報階層]

STYLE
ThinkMove: practical density, calm empathy, white/navy/gray foundation,
restrained teal for forward movement, orange only for one limited emphasis.
Use the selected primary taste consistently with the rest of the deck.

CHROME POLICY
- Page role: [cover / section / content / closing]
- Inherit only: palette, typography, texture, line quality, logo scale.
- Do not inherit cover-specific geometry, diagonal bands, portrait frames, or card positions.
- For content slides, keep the content grid clear to the bottom edge. Do not use a large lower-left or lower-right decorative band.
- If a card, chart, table, or conclusion bar occupies the lower 25%, remove bottom edge decoration entirely.
- Decorative marks must stay within the outer 2-3% perimeter and must not touch, overlap, or become tangent to content.

REFERENCE ROLES
- Image 1 [path]: primary content style reference
- Image 2 [path]: optional page-role anchor
- Image 3 [path]: logo / person / source reference

MUST NOT
- Do not invent numbers, quotes, clients, UI, or achievements.
- Do not add unrelated logos, watermarks, fake signatures, or decorative English.
- Do not reserve a large empty logo area.
- Do not create a sparse poster without decision material.
- Do not leave placeholders for later compositing.
- Do not force repeated decoration when it reduces content spacing.
- Do not copy contact-sheet geometry or treat a contact sheet as an input reference.

OUTPUT
A complete slide image. Include every visible element in the generation itself.
No post-compositing is planned.
```
