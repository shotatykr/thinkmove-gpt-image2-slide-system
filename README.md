# ThinkMove GPT-image2 Slide System

ThinkMoveのスライドを、ロゴ・人物・日本語・図解を含む**完成画像としてGPT-image2で生成する**ための制作システムです。

このリポジトリはHTMLスライド、ネイティブ図形、後処理によるロゴ合成を扱いません。1ページを1枚の完成画像として生成し、不合格ページは画像を局所修正せず再生成します。

## この方式が向く資料

- セミナー、登壇、研修
- コンセプト提案、営業資料の初稿
- 世界観と一体感を優先するストーリーデッキ
- 短時間で完成イメージまで到達したい資料

正確な数表、編集可能なグラフ、厳密なロゴ再現、人物同一性の保証が必要な資料には、[`thinkmove-design-system`](https://github.com/shotatykr/thinkmove-design-system)側の編集可能な制作方式を使います。

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

このリポジトリでは`.agents/skills/thinkmove-gpt-image2-slide/`が唯一の制作入口です。後合成を前提にした旧`thinkmove-style-slide-creator`は併用しません。

## Quick Start

1. [`thinkmove-gpt-image2-slide` skill](.agents/skills/thinkmove-gpt-image2-slide/SKILL.md)を入口にする
2. [`DESIGN.md`](DESIGN.md)と[`STYLE.md`](STYLE.md)で画面と言葉の基準を固定する
3. [`templates/deck-manifest.example.json`](templates/deck-manifest.example.json)からManifestを作る
4. `python3 scripts/validate_manifest.py <manifest.json>`を通す
5. 表紙と標準本文を確認後、4〜5枚ずつGPT-image2で完成画像を生成する
6. `python3 scripts/qa_images.py <manifest.json> <final-dir>`と目視QAを通す
7. `python3 scripts/validate_manifest.py <manifest.json> --release`を通してPPTXへ格納する

```text
source.mdからThinkMoveの資料を作って。
このリポジトリの$thinkmove-gpt-image2-slideを使い、全ページをGPT-image2の完成画像として生成してください。
ロゴや人物写真も参照画像として生成へ含め、後合成はしません。
不正確なページは短い指示へ直して再生成し、最後に全ページをQAしてください。
```

## 生成方式

```text
一次資料 + ブランド参照 + 写真/ロゴ参照 + Few-shot
                         ↓
                 GPT-image2
                         ↓
             完成スライド画像（16:9）+ Manifest
                         ↓
            機械QA・目視QA・再生成（最大3試行）
                         ↓
                 PPTX / PDF格納
```

## 承認済みリファレンス

- [`quiet-proposal-ai-dialogue-seminar-v1`](examples/approved-decks/ai-dialogue-seminar/README.md): 表紙、本文基準、比較、概念図、構造、役割図、タイムライン、結論の8種類。セミナー・研修向けQuiet Proposalの基準作例

contact sheetは人間の連続性確認に使い、生成モデルへはページ役割に近いanchorを1〜2枚だけ渡します。

## リポジトリ構成

```text
├── AGENTS.md
├── DESIGN.md                 # GPT-image2画面設計の正本
├── STYLE.md                  # 言葉・空気・物語の正本
├── brand/                    # design-systemから同期したブランド参照
├── assets/references/        # 生成へ渡すラスタ参照素材
├── system/                   # 制作工程・参照画像・QA・バージョン方針
├── prompts/                  # 生成・再生成プロンプト
├── schemas/                  # deck Manifestの機械検証
├── templates/                # Manifest記入例
├── evals/                    # 固定ケースと回帰評価
├── tastes/                   # 資料目的別のテイスト選択
├── examples/                 # visual reference
└── scripts/                  # contact sheet / PPTX格納 / upstream同期
```

## 2つのシステムの分担

| システム | 完成形 | 強み |
|---|---|---|
| `thinkmove-design-system` | HTML、編集可能スライド、ネイティブ図形 | 正確性、編集性、再利用性 |
| このリポジトリ | GPT-image2による完成画像 | 速度、画面全体の一体感、表現力 |

ブランド参照は独立に複製せず、[`upstream.json`](upstream.json)で同期元を記録します。同期方法は[`system/versioning.md`](system/versioning.md)を参照してください。

## 品質の考え方

生成画像のピクセル一致は保証しません。代わりに、同じManifest、同じapproved reference、同じ生成条件、同じhard fail、同じ人の採点基準を使い、毎回同じ品質ゲートを通します。変更時は[`evals/rubric.md`](evals/rubric.md)の固定5ケースを各3回評価します。

## License

ThinkMove Inc.の制作・検証用リファレンスです。詳細は[`LICENSE`](LICENSE)を参照してください。
