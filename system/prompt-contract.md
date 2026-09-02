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
10. Chrome policy：ページ役割に応じて、継承する装飾と消す装飾を明記する

## Visible Japanese

- 1ページの大見出しは原則1つ
- タイトルは原則45文字以内
- 長い文章を画像内へ詰め込まない
- 見出し以外の主要表示要素は最大5個、主要ラベルは原則28文字以内
- 誤字が出た場合、後載せせず短くして再生成する
- 人名、企業名、数値はsource表記をpromptへそのまま書く
- `copy_locked`の文字は人の承認なしに短縮・言い換えしない

## 禁止

- 「いい感じに」「プロフェッショナルに」だけで任せる
- 複数tasteを同格で混ぜる
- sourceにないKPIや顧客の声を作る
- 後から直す前提のプレースホルダーを作る
- 大きなロゴ空白を予約する
- 表紙固有の斜め帯、写真枠、カード位置を本文へそのまま複製する
- 装飾とカード、結論バー、図解を接触・重複させる
- contact sheetをstyle referenceとして生成モデルへ渡す
- 最大3試行を超えて同じページを再生成し続ける

## Chrome policy

`same visual family`だけでは、生成モデルが基準画像のgeometryまで複製しやすい。本文promptでは次を明記する。

- inherit: palette、typography、texture、line quality、logo scale
- do not inherit: cover geometry、large diagonal bands、portrait frame、cover-specific whitespace
- content-safe perimeter: 外周2〜3%は小さな罫線や点だけ
- bottom rule: 下部にカードまたは結論バーがある場合、下辺の面装飾を置かない
