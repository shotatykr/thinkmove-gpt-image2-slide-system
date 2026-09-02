# Changelog

## Unreleased

- GPT-image2全面生成専用のrepo-scoped skillを追加
- deck Manifest schemaと生成前／release時の検証を追加
- 画像寸法、欠番、採用試行を検査するファイルQAを追加
- 最大3試行、hard fail 0件、90点以上、人の承認をrelease条件として固定
- 5種類の固定ケースと回帰評価rubricを追加
- skill、prompt、schema、quality contractのversion正本を追加
- 表紙固有の斜め帯やgeometryを本文へ継承しないルールを追加
- 表紙基準と本文基準を分離し、本文の下部コンテンツ領域を保護
- 装飾とカード・結論バーの接触をQA項目へ追加
- 初の承認済みデッキ参照`quiet-proposal-ai-dialogue-seminar-v1`を追加
- 完成デッキのcontact sheetと、ページ役割別anchorの使い分けを定義

## 0.2.0 — 2026-09-02

- `DESIGN.md`と`STYLE.md`をトップ階層へ追加
- AIの必須読み込みをトップ階層の2ファイルへ集約
- GPT-image2へ直接渡せないSVG、HTML、QR、CSS実装を削除
- 全tasteを混ぜるcontact sheetを削除し、個別preview参照へ変更
- upstream同期をロゴ、人物、顧客ロゴ、漫画のラスタ参照へ限定

## 0.1.0 — 2026-09-02

- GPT-image2による完成スライド画像の制作契約を定義
- ロゴ、人物写真、日本語、図解を後合成しない方針を追加
- production guide、reference input policy、prompt contract、QAを追加
- ThinkMove design systemのbrand／assets snapshotを同梱
- contact sheetとPPTX格納スクリプトを追加
