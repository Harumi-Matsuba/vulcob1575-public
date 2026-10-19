# Open points

## 1. Symbols not in Tomokiyo's table, or whose value is inferred
| symbol (token) | value used | evidence | status |
|---|---|---|---|
| m-shaped double sign (`m`) | uu / uv | p.33 "trouué" = margin "trouvé" | confirmed by contemporary decipherment (1 instance) |
| ʒ-like curl (`z`) | r | p.33 "decret" | 1 clear instance; elsewhere 3 (m) and ʒ (r) are not separable by shape (see section 2) |
| lone plain small c (`c`) | null | p.33 l.6, p.539 l.4, p.526 | inferred: never needed by the reading |
| flat L-like sign (`L`) | g | seigneur, Borgia, gendarmerie, magesté (p.561); also p.526 | inferred from 6+ words; not in Tomokiyo's table as drawn |
| q with crossbar (`ffx`) | ff | affaire, affection, officier (p.562), difficile (p.563), affoiblir (p.563) | Tomokiyo has "ff?"; confirmed by context |
| box-like q (`qq`) | nn | personnage, bonne, ordonné, connoistre | Tomokiyo's nn; confirmed by context |
| 4 with an extra bar (`gn` / `{gn?}`) | gn? | one instance on p.525 l.1 (first pass); the adjudicated transcription reads qq (nn) there: "connoistre" | resolved as qq in the adjudicated transcription; no independent gn instance |
| stem with an upper-right loop and lower-left bowl | r (context) | p.563 l.1, l.6, l.10; p.565 l.15 ("recevoir", "resolution", "attirer") | written "?"; value inferred from context only |
| three-bar stem with a top-right hook | e (context) | p.563 l.5 ("asseurement") | written "?"; one instance |
| cross in a cup | ? | p.562 l.3 and l.18 ("son fre?e") — looks like r in context, transcribed as VM? | unresolved |
| cross standing on a box (`dq`) | mm | p.562 l.8, p.563 l.7 "comme"; p.285 | Tomokiyo's mm. Two signs written "gn" in the second adjudication renamed dq (marked "?") |

## 2. Shape pairs that the two transcribers and the image adjudication could not separate
- 3 (m) vs ʒ (r): image-based changes to z gave non-words on p.525 (serblable, directerent, tellerent); kept 3 and marked "?" where the adjudicator could not decide.
- p (f) vs φ (m): image-based changes to φ gave non-words on p.525 (mait, maire, mrere, maut, merme); kept p and marked "?".
- qa (q) vs al (a): image-based changes to al gave non-words on p.526 (auon, auenuiron); kept qa and marked "?".
- oc (o) vs t4 (t) vs 4 (a): the recurring cross sign; Codex names it t4 or fl; the image adjudicators could not always decide; the reading o makes the words (vous, son, Monseigneur...). Marked "?" where undecided.
- 9 (d) vs q (l): tail length is a continuum; Codex reads q far more often. Marked "9?" where the tail is long.
- ∂ (i) vs δ (n): the main error of the first pass (p.525: about 35 corrected from the image).

These are listed per position in `xcheck/adjudication_img_<page>.tsv` (decision = ambiguous) and appear as uppercase letters in the key output.

## 3. Code words (plain-letter groups inside the cipher)
| group | proposed meaning | evidence | status |
|---|---|---|---|
| pur bellum | l'Electeur palatin | p.33 margin | confirmed (contemporary decipherment) |
| ucb+ (with smua, sec?) | l'Electeur de Saxe | p.33 margin | confirmed for the whole group; how it splits is open |
| saturnus | the Emperor (Rudolf II) | p.525 "ledit seigneur [saturnus] son frere" (Archduke Matthias's brother); p.440 margin "l'empereur" at the same point (low confidence) | probable |
| Juno | the King of Spain | p.440 margin "le Roy d'Espagne" at "plus Juno" (high confidence, one instance); p.561 "ou du dit [Juno] ou du dit seigneur Archiduc" | probable |
| my | qu'il | p.526 "sur ce [my] escrivit toutes les lettres [my] envoya"; p.562 "[my] semble maintenant", "bonne affection [my] a" | probable (context only) |
| my3, my3θ, mine | short function words (que/qu'il/il?) | p.561 "[my3] est necessaire [my3] se resolve"; p.539 | open |
| nelluy benitow (p.258) | probably l'Electeur palatin et duc Casimir | p.258 margin "Loys Elect. Palatin et duc Casimir" beside these groups | probable (calibration page) |
| manua, manue | a person (Spanish side?) | p.561 "[manue] a dit", p.565 "le susdit [manua]" | open |
| mitte, mime (p.258) | "les autres Electeurs", "du pis qu'ils" ? | p.258 margin at the same places | open |
| mare, nez/mez, totum, bel, mim | ? | deciphered letters p.439–501 (low-confidence alignments by Claude Sonnet 5.5; not included) | open |
| fec, sec, sanc, estre, toe, vib, roc, roe, ar, puis, x | nulls (the reading never needs them) | absent from the margin decipherments where checked (p.33, p.258) | probable |

## 4. Passages not read
- p.570 (one line, 22 symbols): shuffled keys sometimes score as well as the real key (4/1,000; 8/1,000 with table symbols only). No reading is given (the key output looks like "…roit peu ou point de proffit", but one line cannot confirm it).
- p.539 l.2–3: "[my3θ] sont n'avoient charge" and "nonobstant que est · [saturnus] [sanc]" — syntax unclear around the code words.
- p.561 l.1–4 and l.18–19, p.562 l.25–26, p.565 l.9 and l.15–16: partly unreadable or code words.
- p.526 l.9–10, l.13–14: syntax unclear.
- Line ends cut by the binding shadow on p.562.

## 5. Not checked
- No human has checked the transcription or the images (see README).
- Dates: p.539 (2 Nov 1577), p.561 (14 Dec 1577), p.565 (21 Dec 1577), p.525–526 (22 Oct 1577, from the heading on p.523) are read from the page headings; sender attribution (Ancel) follows Tomokiyo's list and is not checked against the signatures.
