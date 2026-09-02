# Deck Manifest Contract

Manifestは、内容、生成条件、参照画像、試行履歴、QAを1デッキ単位で固定する制作記録である。画像生成を始める前に作り、採用判断のたびに更新する。

## 正本

- 機械検証: [`../schemas/deck.schema.json`](../schemas/deck.schema.json)
- 記入例: [`../templates/deck-manifest.example.json`](../templates/deck-manifest.example.json)
- 検証: `python3 scripts/validate_manifest.py <manifest.json>`

## Content budget

- タイトル: 原則45文字以内
- 主要な表示要素: タイトルを除いて最大5個
- 主要ラベル: 原則28文字以内
- 長い説明文を画像内へ置かない
- 上限を超える場合は、文字を小さくせず、ページ分割か短縮案を出す

これは文字数だけで品質を決める規則ではない。人名、引用、法定表記など変更できない文字は`copy_locked: true`にし、無断で短縮しない。

## 試行記録

初回を含む最大試行数は3回。各試行へ以下を残す。

- 使用promptファイル
- 使用参照画像
- 出力ファイル
- 結果: `accepted` / `rejected`
- 不合格理由
- 内容を変更した場合の`copy_change`

2回の再生成でも不合格なら、ページを`blocked`にして人の判断を待つ。

## Release条件

各ページについて以下を満たす。

- `status`が`approved`
- `selected_attempt`が存在する
- `qa.hard_failures`が空
- 6項目の合計点が90以上
- `qa.human_approved`が`true`
- `qa.approved_by`が空ではない

Manifest全体の`release.status`を`approved`にし、最終確認者と日時を記録する。

## Version source

- skill、prompt、schema、quality contract: [`versions.json`](versions.json)
- この制作システムの状態: `git rev-parse HEAD`を`versions.system_commit`へ記録
- 同期元design-system: [`../upstream.json`](../upstream.json)のcommitを`versions.design_commit`へ記録

release時はplaceholderを許可しない。
