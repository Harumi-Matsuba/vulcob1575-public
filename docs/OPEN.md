# 未解決の点

英語版：OPEN.en.md（内容は同じ）

## 1. 友清氏の表にない記号、値を推定した記号
| 記号（名前） | 当てた値 | 根拠 | 状態 |
|---|---|---|---|
| m 形の二重字（`m`） | uu／uv | p.33「trouué」＝余白の「trouvé」 | 当時の解読で確かめた（1例） |
| ʒ 形（`z`） | r | p.33「decret」 | はっきりした例は1つ。ほかでは 3（m）と ʒ（r）を形で分けられない（2節） |
| 単独の平文の小さな c（`c`） | 空字 | p.33 l.6、p.539 l.4、p.526 | 推定：読みで一度も要らない |
| 平らな L 形（`L`） | g | seigneur、Borgia、gendarmerie、magesté（p.561）、p.526 | 6語以上からの推定。友清氏の表の描き方にはない |
| 横線のある q（`ffx`） | ff | affaire、affection、officier（p.562）、difficile、affoiblir（p.563） | 友清氏の表に「ff?」。文脈で確かめた |
| 箱形の q（`qq`） | nn | personnage、bonne、ordonné、connoistre | 友清氏の nn。文脈で確かめた |
| 横線が1本多い 4（`gn`） | gn? | p.525 l.1 の1回目だけ。裁定後は qq（nn）で「connoistre」 | 裁定後は qq。独立の gn の例はない |
| 右上に輪、左下にふくらみのある縦線 | r（文脈） | p.563 l.1・l.6・l.10、p.565 l.15（recevoir、resolution、attirer） | 「?」と書いた。値は文脈だけから |
| 右上に鉤のある三本線 | e（文脈） | p.563 l.5（asseurement） | 「?」。1例 |
| 杯の中の十字 | ? | p.562 l.3・l.18（「son fre?e」）。文脈では r に見えるが VM? と書いた | 未解決 |
| 箱の上の十字（`dq`） | mm | p.562 l.8・p.563 l.7「comme」、p.285 | 友清氏の表の mm。2回目の裁定で「gn」と書かれた2つを dq にした（「?」付き） |

## 2. 2人の書き手と画像での裁定で分けられなかった形の組
- 3（m）と ʒ（r）：p.525 で画像から z に変えると語にならなかった（serblable、directerent、tellerent）。3 に戻し、裁定で決められない所に「?」。
- p（f）と φ（m）：p.525 で画像から φ に変えると語にならなかった（mait、maire、mrere、maut、merme）。p に戻し「?」。
- qa（q）と al（a）：p.526 で画像から al に変えると語にならなかった（auon、auenuiron）。qa に戻し「?」。
- oc（o）と t4（t）と 4（a）：くり返し出る十字形。Codex は t4 や fl と呼ぶ。画像での裁定でも決めきれない所がある。o と読めば語になる（vous、son、Monseigneur など）。決まらない所に「?」。
- 9（d）と q（l）：尾の長さは連続的。Codex は q と読むことがずっと多い。尾の長いものは「9?」。
- ∂（i）と δ（n）：1回目のいちばん多い誤り（p.525 で画像から約35か所を直した）。

位置ごとの一覧は `xcheck/adjudication_img_<頁>.tsv`（decision＝ambiguous）。鍵の出力では大文字になっている。

## 3. 符号語（暗号の中の平文の文字の語）
| 語 | 当てた意味 | 根拠 | 状態 |
|---|---|---|---|
| pur bellum | l'Electeur palatin（プファルツ選帝侯） | p.33 の余白 | 当時の解読で確かめた |
| ucb+（smua・sec を含む?） | l'Electeur de Saxe（ザクセン選帝侯） | p.33 の余白 | まとまりとしては確か。どう分かれるかは未確定 |
| saturnus | l'Empereur（皇帝ルドルフ2世） | 較正の p.258・p.285 で、saturnus の位置の余白（5つの読みの多数決）が「l'empereur」「emper…」。p.440 でも同じ位置の余白が「…ur」。p.525「ledit seigneur [saturnus] son frere」 | p.258 で当時の解読と合った（前後の文字がずれずに合った1例）。p.285・p.440 は位置合わせが弱いが同じ語 |
| Juno | le Roy d'Espagne（スペイン王） | p.440：暗号「… [que] {Juno} avoit voulu …」の横の余白を、独立した3つの読み（Claude Sonnet 5.5 の2人、Codex）がそろって「le Roy d'Espaig[ne] … avoit … voulu」と読む（`calib/codeword_juno_p440.txt`）。p.561「ou du dit [Juno] ou du dit seigneur Archiduc」とも合う | 当時の解読で確かめた（1例） |
| my | qu'il（my z＝qu'ilz） | p.321：暗号「il semble [my]z ayent en ceci intelligence」の横の余白を Codex が「quelz? ay·u·?」、Claude Sonnet 5.5 が「quelz ay·en·」と読む（`calib/readers/cwm_*.txt`）。文脈：p.526「sur ce [my] escrivit … [my] envoya」、p.501「celle [my] faut trouver」、p.449「tout haut [my]z veulent vivre」など | 当時の解読で確かめた（1例）、文脈の例が多い |
| totum | l'Empire か | p.443「les deputez de [totum] assemblez a Francfort」「des autres Estatz de [totum]」、p.258「[mait totum] et que」の余白「l'Empire et que」 | 可能性が高い（余白の読みは不確か） |
| mare、grinter（eviter） | 人物か称号 | p.443「service du [mare]」「en la faveur du [mare]」、「ledit [grinter] a fait des levées」 | 未確定 |
| my3、my3θ、mine | my3＝qu'il（または que）、my3θ＝qu'ilz（θ＝z）、mine my3θ＝du pis qu'ilz | p.258 の余白：「contributions [my3] demande」の位置に「que／qu'il」、「seroient [mine my3θ] porroient」の位置に「du pis qu'ilz」 | my3θ は当時の解読で確かめた（1例）。mine 単独の意味は未確定 |
| nelluy benitow（p.258） | l'Electeur Palatin et duc Casimir か | p.258 でこの語の横の余白に「Loys Elect. Palatin et duc Casimir」 | 可能性あり（較正の頁） |
| manua、manue | 人物（スペイン側?） | p.561「[manue] a dit」、p.565「le susdit [manua]」 | 未確定 |
| Mitte（p.258） | 「dauantage les autres」か | p.258 の同じ位置の余白（前後の文字は合うが、余白の語の切れ目が不確か） | 未確定 |
| principalem（p.258） | et principallement celuy | p.258 の余白 | 当時の解読で確かめた（略記とみる） |
| roe | pour（ros の書き方の揺れか） | p.258 の余白：「souvent [roe] la defense」の位置に「pour」 | 1例 |
| nez／mez、bel、mim | ? | 解読済みの書簡 p.439–501（Claude Sonnet 5.5 による確かさの低い対応。ここには入れていない） | 未確定 |
| fec、sec、sanc、sane、pome、estre、toe、vib、roc、ar、puis、x | 空字 | 確かめた所（p.33、p.258）で余白に対応する語がない（sane pome は p.258 で確認） | 可能性が高い |

## 4. 読めていない所
- p.570（1行・22記号）：対照では 4/1,000（表の記号だけで 8/1,000）と弱いが、p.569 の余白の最後の行に当時の解読「… quil ny reussiroit(?) peu ou point de proffit」があり、鍵の出力と合う（未解読ではなかった）。余白の動詞は、Claude Sonnet 5.5 と Claude Opus 5.5 が「reussiroit」、Codex が「en sera」と読み、決めきれない。
- p.539 l.2–3：「[my3θ] sont n'avoient charge」と「nonobstant que est · [saturnus] [sanc]」。符号語のまわりの文の形が分からない。
- p.561 l.1–4・l.18–19、p.562 l.25–26、p.565 l.9・l.15–16：一部が読めないか、符号語。
- p.526 l.9–10・l.13–14：文の形が分からない。
- p.562 は行末が綴じ目の影で切れている。

## 5. 確かめていないこと
- 書き起こしと画像を、人は確かめていない（README・METHOD.md）。
- 日付（p.539＝1577-11-02、p.561＝1577-12-14、p.565＝1577-12-21、p.525–526＝1577-10-22〔p.523 の見出し〕）は頁の見出しから読んだ。差出人（Ancel）は友清氏の一覧に従い、署名とは照らしていない。
