# Versioning

このリポジトリは、制作方式を独立して更新しながら、ThinkMoveブランド正本との対応を記録する。

## バージョンの分担

- `thinkmove-design-system`: 世界観、theme、公式assetの正本
- `thinkmove-gpt-image2-slide-system`: 全面画像生成のproduction guide、prompt、taste、QA

## 更新方法

1. `upstream.json`の`commit`を更新する
2. `scripts/sync_from_design_system.sh <local-path>`を実行する
3. `git diff`でbrandとassetsの変化を確認する
4. visual referenceとpromptへの影響を確認する
5. `CHANGELOG.md`へ互換性を記録する

同期は自動公開しない。brand更新と生成方式更新を同じリリースへ含める必要はない。

## SemVer

- MAJOR：制作契約、出力形式、必須読み込み順の破壊的変更
- MINOR：taste、prompt、QA、reference assetの追加
- PATCH：誤字、リンク、説明、互換な調整

各releaseは、対応するdesign-system commitを`upstream.json`へ固定する。
