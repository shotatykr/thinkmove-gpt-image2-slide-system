# Examples

- `taste-previews/`: taste選択後に1枚だけ読むvisual reference
- `approved-decks/`: GPT-image2で一括生成し、デッキ全体のQAを通した承認済みreference

これらは現行デザインシステムから移したseed reference。今後、GPT-image2でロゴ・人物・日本語まで一括生成し、QAを通過したreference-quality sampleへ更新する。

全tasteを混ぜたcontact sheetは収録しない。生成モデルへ誤って渡すと、複数のvisual familyを平均化するため。

承認済みデッキは、まず各デッキの`README.md`で用途とanchor mapを確認する。contact sheetは人間の連続性確認用であり、生成モデルへはページ役割に近いanchorを1〜2枚だけ渡す。
