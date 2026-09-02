# Prompt Contract

各スライドのpromptには、少なくとも次を含める。

## 必須項目

1. Page role：表紙、問題提起、診断、手順、事例、結論など
2. Claim：読み手に残す一文
3. Visible Japanese：画像内に描く短い日本語
4. Evidence：数字、発言、画面など
5. Composition：左右、前景・背景、視線の流れ
6. Style：選択したtasteと共通visual family
7. References：各参照画像の役割
8. Must not：架空データ、余計なロゴ、英語化など
9. Output：16:9、完成スライド画像

## Visible Japanese

- 1ページの大見出しは原則1つ
- 長い文章を画像内へ詰め込まない
- 見出しと3〜5個の短い要素を目安にする
- 誤字が出た場合、後載せせず短くして再生成する
- 人名、企業名、数値はsource表記をpromptへそのまま書く

## 禁止

- 「いい感じに」「プロフェッショナルに」だけで任せる
- 複数tasteを同格で混ぜる
- sourceにないKPIや顧客の声を作る
- 後から直す前提のプレースホルダーを作る
- 大きなロゴ空白を予約する
