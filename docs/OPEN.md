# 未解決の点

英語版：OPEN.en.md（内容は同じ）

## 1. 友清氏の表にない記号、値を推定した記号
| 記号（名前） | 当てた値 | 根拠 | 状態 |
|---|---|---|---|
| m 形の二重字（`m`） | uu／uv | p.33「trouué」＝余白の「trouvé」 | 当時の解読で確かめた（1例） |
| ʒ 形（`z`） | r | p.33「decret」 | はっきりした例は1つ。ほかでは 3（m）と ʒ（r）を形で分けられない（§2） |
| 単独の平文の小さな c（`c`） | 空字 | p.33 l.6、p.539 l.4、p.526 | 推定：読みで一度も要らない |
| 平らな L 形（`L`） | g | seigneur、Borgia、gendarmerie、magesté（p.561）、p.526 | 6語以上からの推定。友清氏の表の描き方にはない |
| 横線のある q（`ffx`） | ff | affaire、affection、officier（p.562）、difficile、affoiblir（p.563） | 友清氏の表に「ff?」。文脈で確かめた |
| 箱形の q（`qq`） | nn | personnage、bonne、ordonné、connoistre | 友清氏の nn。文脈で確かめた |
| 横線が1本多い 4（`gn`） | gn? | p.525 l.1 の1回目だけ。裁定後は qq（nn）で「connoistre」 | 裁定後は qq。独立の gn の例はない |
| 右上に輪、左下にふくらみのある縦線 | r（文脈） | p.563 l.1・l.6・l.10、p.565 l.15（recevoir、resolution、attirer） | 「?」と書いた。値は文脈だけから |
| 右上に鉤のある三本線 | e（文脈） | p.563 l.5（asseurement） | 「?」。1例 |
| 杯の中の十字 | ? | p.562 l.3・l.18（「son fre?e」）。文脈では r に見えるが VM? と書いた | 未解決 |

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
| saturnus | 皇帝（ルドルフ2世） | p.525「ledit seigneur [saturnus] son frere」（大公マティアスの兄）。p.440 で同じ位置の余白に「l'empereur」（確かさ低） | 可能性が高い |
| Juno | スペイン王 | p.440 で「plus Juno」の横の余白が「le Roy d'Espagne」（確かさ高、1例）。p.561「ou du dit [Juno] ou du dit seigneur Archiduc」 | 可能性が高い |
| my | qu'il | p.526「sur ce [my] escrivit toutes les lettres [my] envoya」、p.562「[my] semble maintenant」「bonne affection [my] a」 | 可能性が高い（文脈だけ） |
| my3、my3θ、mine | 短い語（que／qu'il／il?） | p.561「[my3] est necessaire [my3] se resolve」、p.539 | 未確定 |
| nelluy benitow（p.258） | l'Electeur Palatin et duc Casimir か | p.258 でこの語の横の余白に「Loys Elect. Palatin et duc Casimir」 | 可能性あり（較正の頁） |
| manua、manue | 人物（スペイン側?） | p.561「[manue] a dit」、p.565「le susdit [manua]」 | 未確定 |
| mitte、mime（p.258） | 「les autres Electeurs」「du pis qu'ils」か | p.258 の同じ位置の余白 | 未確定 |
| mare、nez／mez、totum、bel、mim | ? | 解読済みの書簡 p.439–501（AI のサブエージェントによる確かさの低い対応。ここには入れていない） | 未確定 |
| fec、sec、sanc、estre、toe、vib、roc、roe、ar、puis、x | 空字 | 確かめた所（p.33、p.258）で余白に対応する語がない | 可能性が高い |

## 4. 読めていない所
- p.539 l.2–3：「[my3θ] sont n'avoient charge」と「nonobstant que est · [saturnus] [sanc]」。符号語のまわりの文の形が分からない。
- p.561 l.1–4・l.18–19、p.562 l.25–26、p.565 l.9・l.15–16：一部が読めないか、符号語。
- p.526 l.9–10・l.13–14：文の形が分からない。
- p.562 は行末が綴じ目の影で切れている。

## 5. 確かめていないこと
- 書き起こしと画像を、人は確かめていない（README）。
- 日付（p.539＝1577-11-02、p.561＝1577-12-14、p.565＝1577-12-21、p.525–526＝1577-10-22〔p.523 の見出し〕）は頁の見出しから読んだ。差出人（Ancel）は友清氏の一覧に従い、署名とは照らしていない。
