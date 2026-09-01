# Reference Assets

`references/`には、GPT-image2へ渡すThinkMoveのブランド参照素材を収録する。

- `logo.png`: ロゴ参照
- `profile/`: 人物参照
- `logos/`: 公開許諾済み顧客ロゴ参照
- `manga/`: 4コマの表現参照
- `icons/`: モチーフと線の参照
- `diagrams/`: 図解構造の参照
- `frames/`: 画面表現の参照
- `qr/`: QRの存在・配置参照。読み取り保証はしない

これらを最終画像へ後合成しない。モデルへ参照として渡し、完成画像の一部として生成する。

正確なロゴ、QR読み取り、人物同一性が完了条件なら、この制作方式は使わない。

同期元とcommitは[`../upstream.json`](../upstream.json)を参照する。
