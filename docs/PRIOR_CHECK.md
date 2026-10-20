# 先行の反証調査

英語版：PRIOR_CHECK.en.md

目的：このリポジトリの読み（BnF Cinq Cents de Colbert 398 の p.525–526、p.539、p.561–563、p.565、p.570 の暗号部分。Guillaume Ancel の1577年10〜12月の書簡）が、すでに誰かに読まれ公表されていないかを、「すでに読まれている」と示すつもりで探した。

## 結論
- 区分：**見つからない**（下の調べた先では、これらの暗号部分の解読は見当たらない。2026-10-20 時点）。
- 「初めて」とは書かない。下の「確かめられなかった先」が残る。
- 近い先行の扱い：
  - 鍵は友清理士氏の復元（Cryptiana）。同氏は、この鍵で未解読の書簡が読めると書いているが、読みは載せていない。
  - Damien Fontvieille 氏の発表（2024年4月）は Jean de Vulcob の1570年代の暗号通信を扱い、学会報告によれば、鍵がないため、行間にすでにある当時の解読を使って分析している。ここで読んだ Ancel の1577年の、当時の解読がない部分とは重ならない。
  - G. Labouchère（1923）の Ancel 研究は、同じ1577年10月22日の書簡の**平文の段落**（オーストリアの諸身分の誓い）を要約しているが、暗号の部分の内容には触れていない。

## 1. 解読に加わっていない読み手による調査（2026-10-20）
解読の作業に加わっていない別の読み手（Claude）が、解読の記録を受け取り、「すでに読まれている」と示すつもりで探した。

| 先 | 版・日付 | 結果 |
|---|---|---|
| Cyphersolver（dbourdeau/cyphersolver） | origin/main 0258b8ab（2026-10-18） | 「Colbert 398」は vulcob1573（BnF fr.3318、G. Lasry）の比較鍵の記述だけ。「Malstet」「Varembon」0件 |
| Cyphersolver の issue・PR | 全件（最新 #49、2026-10-19） | 該当なし |
| Lasry 氏の論文抜粋（Cyphersolver 内） | 同上 | Vulcob は出てこない |
| Cryptiana unsolved.htm／GL.htm／ai.htm／verification.htm | 2026-10-13／10-15／10-19／10-15 | Colbert 398 は GL.htm で fr.3318 の比較鍵としてだけ |
| Cryptiana frencheastern.htm | 2026-03-15 | 鍵の出典。書簡の一覧と「The reconstructed key below will allow reading undeciphered letters」。解読文はない |
| Cryptoole API | 全854件 | 項目なし |
| DECODE の目録の写し（aaymeloglu/unsolved-ciphers、c2436b0、2026-09-18） | 10,106件 | Colbert 398 の記録なし、「Vulcob」0件 |
| GitHub コード検索「"Colbert 398"」（14件）・「Vulcob」 | 2026-10-20 | Cyphersolver の vulcob1573、NoAutopilot/cipher-lab の birago-nevers-1571（Colbert 398 の**数字**暗号の表を別の暗号に当てて不一致）など。Ancel の1577年の暗号の読みはない |
| NoAutopilot/cipher-lab | pushed 2026-10-19 | 「Vulcob」は fr4735（1573）と vulcob1573 の対照表だけ |
| BravoBravoIX・pangoleen/cipher-readings・el-descifrador/cabinet-noir | 2026-10-20 | 該当なし（ファイル名・リポジトリ名で判定） |
| Fontvieille 氏の別稿（Cahiers Jean-Mabillon 2、2021） | PDF の文字層 | 「398」0件、「chiffr」0件、「Vulcob」1件（Morvillier の甥として） |
| Web 検索：Ancel の1577年の書簡の刊本 | 2026-10-20 | 見つからない |

## 2. 解読をした読み手による追加の調査（2026-10-20）
上の調査と重ならない先を中心にした。

| 先 | 何をしたか | 結果 |
|---|---|---|
| H-Soz-Kult の学会報告（L. Oberdorfer, « Kryptographie in Theorie und Praxis im deutsch-französischen Kontext (1300–1800) », H-Soz-Kult, 18.11.2024, conferencereport fdkn-151312） | 直接はボット確認で開けず、Internet Archive の保存（2024-12-05）を読んだ | Fontvieille 氏の発表の要約：Vulcob の1570年代の書簡の暗号化された3分の1は、鍵がないが、行間に一部すでにある解読によって分析できる、という趣旨。Ancel・1577年・Colbert 398 の頁の解読には触れていない |
| 同じ学会の論文集 | フランス外務省の電子図書館「Art du chiffre」の注記 | 「C. Desenclos, S. Externbrink, E. Szarka et J. Ulbert (dir.), *Entre France et Allemagne. Théorie et pratique cryptographiques (1300-1800)*, dossier à paraître dans *Zeitschrift für Historische Forschung*」。刊行されたかは確かめられなかった（出版社のページが 403） |
| G. Labouchère, « Guillaume Ancel, envoyé résident en Allemagne, 1576-1615 », *Revue d'histoire diplomatique* 37 (1923) | Internet Archive の全文（revue-d-histoire-diplomatique_1923_37、OCR）を検索し、該当の頁を読んだ | 論考は「Colbert 398」を7回出典に挙げる。1577年10月22日の書簡については、平文の段落（オーストリアの諸身分が大公エルンスト・マティアス・マクシミリアンの前で皇帝に誓った件）だけを要約している。巻全体で「déchiffr」0件、「Malstet」「Varembon」「Varambon」「Borgia」0件、「chiffre」4件（いずれも数の意味） |
| HistoCrypt 2026（アミアン、6月22–25日） | histocrypt.org/program/ の口頭発表一覧 | Vulcob・Ancel・Colbert 398 の発表なし（ポスターの題目は見ていない） |
| Gallica の刊行物 | 検索 API：「Colbert 398」（写本以外） | 33件。題名に暗号・Vulcob・Ancel に関わるものはない |
| Cryptiana の全記事 | 目次（crypto.htm）の287本を取得して検索 | 「Colbert 398」は GL.htm・danzay.htm・frencheastern.htm・frenchnumerical.htm だけ（鍵の出典、Danzay の p.63、数字の暗号、fr.3318 の比較鍵）。「Ancel」は frencheastern・frenchnumerical（1601–02年の別の暗号）・henryiii・henryiv・louisxiii。どれもこれらの頁の読みを載せていない |
| Lasry 氏の論文 | ウェブ検索（Cryptologia 2026、ResearchGate、academia.edu） | Colbert 398 に関わる論文は見当たらない（一覧のページそのものは開いていない） |
| マティアス大公のネーデルラント行き（1577）の研究 | ウェブ検索（仏・英・独）：Malstet、Varambon、Borgia、Ancel | フランス大使の暗号の報告を使った記述は見当たらない |

## 確かめられなかった先
- ZHF の特集（上の論文集）。2026年1号（Vol. 53, Issue 1）の目次（出版社の電子版、2026-10-20）には暗号の論考も編者の名前もない。2号以降は出版社の電子版にまだ見当たらない。
- Google Books・HathiTrust の全文検索（Ancel の書簡の刊本）。Google Books の API は 2026-10-20 に2回とも 429（回数の上限）。
- DECODE の記録の文書一覧（ログインが要る。ただし目録に Colbert 398 の記録はない）。
- Lasry 氏の未公開の解読。

## 公表前の見直し（2026-10-20 08:40〜08:50 JST）
解読に加わっていない読み手が、上の確かめの後に新しい動きがないかを、主な先で見直した。区分は「見つからない」のまま。
| 先 | 日付・版 | 結果 |
|---|---|---|
| Cyphersolver の台帳 | origin/main 0258b8ab（2026-10-18、変わっていない） | Colbert 398 の Ancel の書簡の項目はない |
| 同 issue | #51 まで（2026-10-19） | 題名と本文で「Vulcob」「Ancel」「Colbert 398」：当たりなし |
| Cryptiana frencheastern.htm | Last-Modified 2026-03-15（変わっていない） | 読みの追加なし |
| GitHub のコード検索 | 2026-10-20 | 「"Colbert 398"」：NoAutopilot/cipher-lab と cyphersolver だけ。cipher-lab の当たりは birago-nevers-1571 の数字暗号の表など、上の表に書いたものと同じ |

## 公開後の見直し（2026-10-20 00:56 UTC）
| 先 | 結果 |
|---|---|
| Cyphersolver の台帳（origin/main 0258b8ab、変わっていない）と issue（#54 まで） | Colbert 398 に関わる issue は、このリポジトリの報告（#53）だけ |
| Cryptiana unsolved.htm（Last-Modified 2026-10-19 23:08 GMT）・GL.htm（10-15）・frencheastern.htm（03-15） | 更新は別の項目。Colbert 398・Vulcob・Ancel の記述なし |
| GitHub コード検索「"Colbert 398"」 | NoAutopilot/cipher-lab と Cyphersolver だけ（前回と同じ） |
| NoAutopilot/cipher-lab の 2026-10-19 12:00 UTC 以降のコミット70件と ciphers/ | Colbert 398・Ancel・Vulcob に関わるものなし |
