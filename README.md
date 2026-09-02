# ThinkMove GPT-image2 Slide System

ThinkMoveのスライドを、ロゴ・人物・日本語・図解を含む**完成画像としてGPT-image2で生成する**ための制作システムです。

このリポジトリはHTMLスライド、ネイティブ図形、後処理によるロゴ合成を扱いません。1ページを1枚の完成画像として生成し、不合格ページは画像を局所修正せず再生成します。

## この方式が向く資料

- セミナー、登壇、研修
- コンセプト提案、営業資料の初稿
- 世界観と一体感を優先するストーリーデッキ
- 短時間で完成イメージまで到達したい資料

正確な数表、編集可能なグラフ、厳密なロゴ再現、人物同一性の保証が必要な資料には、[`thinkmove-design-system`](https://github.com/shotatykr/thinkmove-design-system)側の編集可能な制作方式を使います。

## Quick Start

1. [`AGENTS.md`](AGENTS.md)を読む
2. [`DESIGN.md`](DESIGN.md)と[`STYLE.md`](STYLE.md)で画面と言葉の基準を固定する
3. [`system/production-guide.md`](system/production-guide.md)に沿って資料の目的とタイトル列を決める
4. [`prompts/deck-orchestrator.md`](prompts/deck-orchestrator.md)と[`prompts/base-slide.md`](prompts/base-slide.md)を使って各ページを生成する
5. [`system/qa-checklist.md`](system/qa-checklist.md)で全ページを確認する
6. 必要ならcontact sheetとPPTXへ格納する

```text
source.mdからThinkMoveの資料を作って。
このリポジトリのAGENTS.mdを入口に、全ページをGPT-image2の完成画像として生成してください。
ロゴや人物写真も参照画像として生成へ含め、後合成はしません。
不正確なページは短い指示へ直して再生成し、最後に全ページをQAしてください。
```

## 生成方式

```text
一次資料 + ブランド参照 + 写真/ロゴ参照 + Few-shot
                         ↓
                 GPT-image2
                         ↓
             完成スライド画像（16:9）
                         ↓
                 目視QA・再生成
                         ↓
                 PPTX / PDF格納
```

## リポジトリ構成

```text
├── AGENTS.md
├── DESIGN.md                 # GPT-image2画面設計の正本
├── STYLE.md                  # 言葉・空気・物語の正本
├── brand/                    # design-systemから同期したブランド参照
├── assets/references/        # 生成へ渡すラスタ参照素材
├── system/                   # 制作工程・参照画像・QA・バージョン方針
├── prompts/                  # 生成・再生成プロンプト
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

## License

ThinkMove Inc.の制作・検証用リファレンスです。詳細は[`LICENSE`](LICENSE)を参照してください。
