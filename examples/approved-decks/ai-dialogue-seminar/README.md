# Approved reference: AI dialogue seminar

## Reference ID

`quiet-proposal-ai-dialogue-seminar-v1`

GPT-image2で日本語、ロゴ、図解まで一括生成し、20枚の連続性をQAしたセミナーデッキから、公開可能な8枚だけを抜き出した承認済みvisual reference。

Primary tasteは`Quiet Proposal`。登壇資料や研修資料でも、落ち着いた実務密度、結論型タイトル、白地の余白、navyとtealの線画を優先するときに使う。

## 最初に見るもの

- [`contact-sheet.png`](contact-sheet.png): 表紙から結論までのリズム確認用。生成モデルへは渡さない
- [`anchors/02-content-baseline.png`](anchors/02-content-baseline.png): 標準的な本文ページの第一参照
- [`anchors/19-timeline.png`](anchors/19-timeline.png): 高密度な手順ページの第二参照

## Anchor map

| File | Role | 参照するもの |
|---|---|---|
| `01-cover.png` | 表紙 | タイトルの強さ、限定的な左下装飾、余白 |
| `02-content-baseline.png` | 本文基準 | 白地、文字階層、カード間隔、下部余白 |
| `03-comparison-graph.png` | 比較 | 線グラフを主役にする密度と視線誘導 |
| `07-concept-visual.png` | 概念図 | 画面中央の大きな比喩と短い補足 |
| `10-structured-process.png` | 構造 | 複数項目を表ではなく制作工程として見せる方法 |
| `13-role-diagram.png` | 関係図 | 円の重なり、役割の分解、結論の置き方 |
| `19-timeline.png` | 手順 | 高密度でも下辺を空けるタイムライン |
| `20-closing-loop.png` | 結論 | 冒頭命題への回答と循環する次の一手 |

## 使用ルール

1ページに渡すstyle referenceは1〜2枚に絞る。通常は`02-content-baseline.png`を使い、ページの役割に近いanchorを1枚だけ追加する。

継承する:

- 白、navy、gray中心のpalette
- tealの限定的な前進表現
- 結論型タイトルの文字階層
- 細い線、淡い円、控えめな陰影
- 内容ごとにgeometryを変えても同じ資料に見えるvisual family
- 下部の明確な余白

固定しない:

- 表紙の左下斜め帯
- カード数、カード位置、図の形
- すべてのページへの同じ結論バー
- ロゴのためだけの広い空白

## QA evidence

- Built-in image generationで完成画像として生成
- HTML、SVG組版、文字後載せ、ロゴ後合成なし
- 1672×941px、RGB、16:9
- 日本語、ページ間の論理、装飾と内容の接触を目視確認
- 初回の20枚版に含まれた企業事例5枚は、掲載許可と成果数値の確認前なので公開リファレンスから除外
