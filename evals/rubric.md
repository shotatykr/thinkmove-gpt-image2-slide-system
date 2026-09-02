# Quality regression rubric

スキル、prompt、model、reference、DESIGN.mdのいずれかを変更したとき、[`cases.json`](cases.json)の5ケースを各3回生成する。単発の成功画像ではなく、同じ条件での合格率を比較する。

## 記録する指標

- first-pass rate: 初回生成で合格したページの割合
- pass@3: 最大3試行以内に合格したページの割合
- hard-fail rate: 1回以上hard failが出た割合
- mean attempts: 採用までの平均試行数
- mean human score: 100点評価の平均
- ambiguity log: 実行者がManifest外で判断した内容

## 比較方法

1. 変更前のskill、prompt、reference、design commitを記録する。
2. 5ケースを各3回生成し、基準値を保存する。
3. 変更後も同じ入力、同じ出力サイズ、同じqualityで実行する。
4. hard failの新規分類がないか確認する。
5. pass@3が下がる、hard-fail rateが上がる、または人の平均点が3点以上下がる場合は変更を採用しない。

絶対閾値は最初の基準計測後に固定する。モデル生成は確率的なため、画像のピクセル一致を評価しない。

## Critical checks

各ケースの`critical_checks`は1項目でも不合格ならhard fail。総合点で相殺しない。

人の採点は`.agents/skills/thinkmove-gpt-image2-slide/references/output-contract.md`の100点評価を使う。可能なら同じ評価者が変更前後をblindで比較する。
