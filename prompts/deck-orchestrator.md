# Deck Orchestrator Prompt

```text
sourceをもとに、ThinkMoveのスライド資料を作成してください。

目的:
- Audience: [誰が読むか]
- Job: [資料の仕事]
- Decision: [決めてほしいこと]
- Takeaway: [中心結論]
- Format: [口頭説明 / 単独閲覧]

制作方式:
- 全ページをGPT-image2による16:9の完成画像として生成する
- HTML、ネイティブ図形、文字後載せ、ロゴ後合成は使わない
- ロゴ、人物、写真、図解も参照画像として生成へ含める
- 可視の日本語が誤っていたら、短くしてページごと再生成する

工程:
1. sourceから確認済みの事実と不足情報を分ける
2. Audience / Job / Decision / Takeaway / Evidenceを固定する
3. タイトルだけで全体の論理を作る
4. 各ページのClaim / Evidence / Visual job / Must render / Referencesを定義する
5. primary tasteを1つ選ぶ
6. 表紙基準と、標準的な情報量を入れた本文基準を別々に生成する
7. 本文へ継承するのはpalette、typography、texture、線の品質だけとし、表紙固有のgeometryや斜め帯は継承しない
8. QA checklistを通し、不合格ページだけ再生成する
9. contact sheetとPPTXを作る

sourceにない数字、成果、引用、顧客情報を作らないでください。
```
