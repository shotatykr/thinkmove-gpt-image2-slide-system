# Assets Manifest

各画像の **意味役割**を明記。AI デザインツールは、このインデックスを見て「どの画像をどの文脈で使うか」を判断する。

**原則**: 収録されている画像は全て **固有の semantic weight** を持つ。装飾・重複・LP再現のための画像は含まれない。

---

## Company Mark

| Path | Role |
|------|------|
| [`logo.png`](./logo.png) | 公式ThinkMoveワードマーク（navy accent、2700×571、透過PNG）。ヘッダー／フッター／favicon 等のブランド識別用途全般に使用。**これが唯一のcanonical。** |

---

## Client Logos（WORKS コンポーネント demo）

「実績紹介」セクションのロゴグリッド用。4社で完結。

| Path | Client |
|------|--------|
| [`logos/makuake_logo.png`](./logos/makuake_logo.png) | 株式会社マクアケ（クラウドファンディング） |
| [`logos/zigexn-logo.png`](./logos/zigexn-logo.png) | 株式会社じげん |
| [`logos/collabit-logo.png`](./logos/collabit-logo.png) | 株式会社コラビット（HowMa） |
| [`logos/freeweb-logo.png`](./logos/freeweb-logo.png) | 株式会社フリーウェブホープ |

---

## 4コマ漫画（Carousel module demo）

LP トップの「こんな経験、ありませんか？」セクションで使用される4コマ漫画カルーセル。worldview の核である「重たい話を、重たく伝えない」の象徴。LP では5枚あるが、demo としては3枚で carousel の機能（slide遷移、opacity変化、dot navigation）を示すのに十分。

| Path | Scene（alt） |
|------|------|
| [`manga/4koma_comic_A.webp`](./manga/4koma_comic_A.webp) | 週2時間で、止まっていた時間が動き出す。 |
| [`manga/4koma_pattern_B.webp`](./manga/4koma_pattern_B.webp) | ChatGPTだけで止まっていませんか。最適な組み合わせを、一緒に見つけましょう。 |
| [`manga/4koma_pattern_C.webp`](./manga/4koma_pattern_C.webp) | 認識のズレが、チームの推進力を奪っていた。 |

**使用コンテキスト**: `.tm-manga` カルーセル（slide 45% width、scale 0.88→1.0、opacity 0.35→1.0、blur 1px→0）。dot nav は teal `#0D9488`。

---

## 代表ポートレート（media-text layout demo）

| Path | Role |
|------|------|
| [`profile/toyokura-shota.jpg`](./profile/toyokura-shota.jpg) | 代表取締役 **豊藏翔太**。森の背景、黒シャツ、1108×1477、JPEG。`media-text` レイアウト（COMPANYセクション、代表紹介ブロック）で使用。**「この人がやっている会社」という属人性の軸**。 |

**禁止表記**: 「豊倉」「豊蔵」は誤り。**「豊藏」（旧字体）が唯一の正**。

---

## 収録方針

本 manifest に**含まれない**画像の例（= 思想上不要）：

- LP のフルページスクリーンショット（文章で再現可能、context-sufficient）
- 背景ストック写真（MacBook + コーヒー等、unique な semantic weight なし）
- 同一人物の別背景写真（重複）
- 動的に生成される OGP や blog サムネ（役割が画像本体でなく、文章と URL で十分）

**判断軸**: 「その画像が無いと worldview / component demo が成立しないか？」
YES → 収録。NO → 削除。
