# AGENTS.md — GPT-image2 slide entry point

このリポジトリは、ThinkMoveのスライドを**1ページ1枚の完成画像としてGPT-image2で生成する**ための正本です。

## 最初に読む順番

1. `AGENTS.md`
2. `DESIGN.md`
3. `STYLE.md`
4. `system/production-guide.md`
5. `system/reference-input-policy.md`
6. `system/prompt-contract.md`
7. 用途に合う`tastes/*.md`を1つだけ
8. `prompts/base-slide.md`
9. 必要時だけ`brand/worldview/`と`brand/theme/design.json`
10. 出力前に`system/qa-checklist.md`

全taste、全画像、全promptを同時に読まない。資料用途に必要な参照だけを選ぶ。

## 制作契約

- スライド本文、ロゴ、人物、図解を含む完成画面をGPT-image2で生成する
- HTML、SVG組版、ネイティブ図形、ロゴ後合成、文字後載せを使わない
- 可視の日本語が間違っていたら、短くして再生成する
- 画像を局所パッチして完成扱いにしない
- 1ページ1メッセージだが、数字・根拠・手順・次の一手を薄くしない
- sourceにない数字、成果、引用、顧客情報を作らない
- 一次情報が不足する場合は、一般論で埋めず不足を報告する
- 全ページを同じ比率、同じvisual familyで生成する
- 最後にcontact sheetで連続性を確認する

## 参照画像

`assets/references/`のロゴ、写真、漫画は、生成モデルへ渡すラスタ参照素材です。最終画像へピクセル単位で貼り付ける素材ではありません。

参照画像を使っても、ロゴ形状や人物の同一性は完全には保証されません。完全一致が完了条件なら、この方式を使わず編集可能な制作方式へ切り替えます。

## ブランドの核

- 白、navy、grayを主役にする
- tealは前進、orangeは限定的な注意・変化に使う
- 実務密度のある冷静な共感
- 余白だけのポスターにしない
- 煽らない、盛らない、一般論で逃げない
- ロゴのために大きな空白を確保しない

## 出力

推奨構成:

```text
outputs/<deck-slug>/
├── source/
├── prompts/
├── raw/
├── final/
├── contact-sheet.png
├── final.pptx
└── qa.md
```

`raw/`と`final/`が同一でもよい。`final/`にはQAを通過した画像だけを置く。
