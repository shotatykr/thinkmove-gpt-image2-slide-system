# Output contract

## 推奨出力構成

```text
outputs/<deck-slug>/
├── source/
├── manifest.json
├── prompts/
├── raw/
├── final/
├── qa-images.json
├── contact-sheet.png
├── final.pptx
└── qa.md
```

`raw/`は全試行、`final/`は採用画像だけを保持する。生成画像を加工して`final/`へ移してはいけない。

## Hard fail

- sourceと異なるタイトル、固有名詞、数字、単位、期間
- sourceにない事実、成果、引用、顧客、画面、グラフ
- 指定外のロゴ、透かし、署名、装飾英語
- 重要な文字や図の見切れ、接触、重なり
- 16:9ではない、指定サイズではない、欠番がある
- ページのClaimと生成画像の意味が一致しない
- HTML、文字後載せ、ロゴ後合成、局所パッチを利用した

## 100点評価

| 項目 | 配点 |
|---|---:|
| source fidelity | 30 |
| readability / Japanese | 20 |
| visual family | 20 |
| layout / spacing | 15 |
| narrative role | 10 |
| brand handling | 5 |

合計90点以上でも、hard failが1件あれば不合格。

## 人が確認すること

- 3秒でページの役割が分かる
- 30秒で判断材料と次の一手を説明できる
- 表紙固有のgeometryが本文へ反復されていない
- 装飾より内容の余白が優先されている
- contact sheetで論理、密度、色、人物表現が連続している
- 公式ロゴや本人写真のピクセル一致を誤って保証していない
