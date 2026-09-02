# Reference Assets

`references/`には、GPT-image2へ渡すThinkMoveのブランド参照素材を収録する。

- `logo.png`: ロゴ参照
- `profile/`: 人物参照
- `logos/`: 公開許諾済み顧客ロゴ参照
- `manga/`: 4コマの表現参照

これらを最終画像へ後合成しない。モデルへ参照として渡し、完成画像の一部として生成する。

SVGアイコン、図解部品、ブラウザ枠、QRは収録しない。GPT-image2へ直接渡すラスタ参照ではなく、正確な再現も期待できないため。

正確なロゴ、QR読み取り、人物同一性が完了条件なら、この制作方式は使わない。

同期元とcommitは[`../upstream.json`](../upstream.json)を参照する。
