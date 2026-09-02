---
name: thinkmove-gpt-image2-slide
description: ThinkMoveのセミナー資料、登壇資料、提案デッキを、文字・ロゴ・人物・図解まで含むGPT-image2の16:9完成画像として制作・再生成・QAする。HTML、編集可能スライド、後合成が必要な依頼には使わない。
---

# ThinkMove GPT-image2 Slide

1ページを1枚の完成ラスタ画像として作る。文字、ロゴ、人物、写真、図解を生成画像内に含め、後工程で重ねない。

このリポジトリでは、後合成を前提にした旧`thinkmove-style-slide-creator`を併用しない。このskillを唯一の制作入口にする。

## 制作前に読む

リポジトリルートを、このファイルから`../../..`として解決する。

1. ルートの`DESIGN.md`
2. ルートの`STYLE.md`
3. `system/production-guide.md`
4. `system/manifest-contract.md`
5. `system/reference-input-policy.md`
6. 新しいvisual familyを選ぶ必要がある場合だけ`tastes/README.md`
7. 選択した`examples/approved-decks/*/README.md`を1つだけ

画像を生成・編集するときは、利用環境の`imagegen` skillも読み、その生成手順に従う。

## 方式の境界

- 常に`image-native`方式を使う。
- HTML、SVG組版、ネイティブ図形、文字後載せ、ロゴ後合成、顔の差し替えを使わない。
- ロゴや人物写真はラスタ参照として生成モデルへ渡す。最終画像へ貼り付けない。
- ロゴ形状、人物同一性、長い日本語のピクセル単位の完全一致を完成条件にしない。
- 完全一致や編集可能性が必要なら生成を開始せず、HTML／編集可能スライド方式が必要だと報告する。

## 実行契約

### 1. 入力を固定する

一次資料を確認し、`templates/deck-manifest.example.json`を基にデッキManifestを作る。

- Audience、Job、Decision、Takeawayを確定する。
- sourceにない数字、引用、顧客情報、UI、実績を作らない。
- 豊藏固有の一次情報が2つ未満なら、一般論で埋めず素材不足を報告する。
- 全ページのタイトルを先に並べ、タイトルだけで論理が追える状態にする。
- 各ページのClaim、Evidence、Visual job、Visible Japanese、anchorをManifestへ保存する。
- `system/versions.json`と`upstream.json`を使い、skill、prompt、制作システムcommit、design-system commitを固定する。

Manifestを作成したら、画像生成前に次を実行する。

```bash
python3 scripts/validate_manifest.py path/to/manifest.json
```

依存パッケージがない場合は、勝手に別方式へ切り替えず、許可された環境で`requirements.txt`を導入してから再実行する。

### 2. visual familyを固定する

- 既存の承認済みデッキが用途に合う場合、そのreference IDをManifestへ記録する。
- 通常の本文は`02-content-baseline.png`を第一参照にする。
- 必要ならページ役割に近いanchorを1枚だけ追加する。
- 表紙には表紙anchorを使えるが、表紙固有の斜め帯やgeometryを本文へ継承しない。
- contact sheetを生成モデルへの参照画像にしない。
- 合う承認済みデッキがない場合、表紙1枚と標準本文1枚だけを先に生成し、人の承認後に続行する。

### 3. ページ単位で生成する

`prompts/base-slide.md`を、Manifestの1ページ分で埋める。

- 出力はManifest指定の16:9サイズ、原則high quality。
- exact textは引用符で囲み、数字・人名・会社名をsourceどおりに明記する。
- 参照画像には役割を付ける。
- 変えてよいものと維持するものを分ける。
- 後処理用の空白、仮ロゴ、プレースホルダーを作らない。

最初に表紙と標準本文を確認する。その後は4〜5枚単位で生成し、各バッチで個別画像とcontact sheetを確認する。

### 4. 不合格ページを再生成する

`prompts/regeneration.md`を使い、不合格理由を1〜3点に絞る。

- 局所パッチや文字の上書きをしない。
- 1ページの最大試行数は初回を含め3回。
- 修正は1回につき1テーマを優先する。
- 重要な不変条件は再生成のたびに書き直す。
- 2回の再生成でも通らない場合は停止する。文字短縮などの内容変更案を人へ提示し、無断で意味を変えない。
- すべての試行と不合格理由をManifestへ記録する。

### 5. QAして格納する

まず機械検査を実行する。

```bash
python3 scripts/qa_images.py path/to/manifest.json path/to/final
```

次に`system/qa-checklist.md`で意味・日本語・余白・連続性を目視確認し、Manifestへ採点と承認者を記録する。完成判定は次の両方を満たす場合だけ。

- hard failが0件
- 総合スコア90点以上かつ`human_approved: true`

最後にrelease検証を実行する。

```bash
python3 scripts/validate_manifest.py path/to/manifest.json --release
```

合格画像だけを`final/`へ置き、contact sheetとPPTXを作る。PPTX格納後も見切れや順序を再確認する。

## 完了報告

- 出力先
- 使用したroute、skill version、prompt version、reference ID
- 初回合格率、再生成ページ、最大試行数
- QA結果と残る制約
- ロゴ・人物は生成による再現であり、公式素材のピクセル一致ではないこと

詳細な合否判定と出力構成は[references/output-contract.md](references/output-contract.md)を必要時に読む。
