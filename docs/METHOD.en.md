# Method, numbers, AI use and limits

## Material
- BnF, Cinq Cents de Colbert 398 (Gallica ark:/12148/btv1b525218133): original letters to Charles IX, Henry III and Catherine de Médicis on the affairs of Germany, including dispatches of Jean de Vulcob (1575–76) and Guillaume Ancel (1576–78, 1584), French residents at the Imperial court. Page numbers are the manuscript pagination; "f" numbers are Gallica views (see SOURCES.md for the page→view table).
- Key: S. Tomokiyo's reconstruction "Vulcob and Ancel's Cipher (1575–1584)" (Cryptiana, `code/frencheastern.htm`, image `easternVulcob.png`; page Last-Modified 15 Mar 2026). Tomokiyo lists the letters and writes that the key "will allow reading undeciphered letters"; he does not publish readings of them.
- Images were viewed and cut from the BnF IIIF service (2400 px wide). No image is redistributed here.

## Which passages were undeciphered
All cipher pages listed by Tomokiyo were viewed. Most carry a contemporary decipherment in the left margin. The cipher on p.525–526, p.539, p.561–563, p.565 and the single cipher line on p.570 has none; these are the passages read here (125 cipher lines, 4,377 symbols in the final transcription).

## Steps
1. **Key table** (`data/key.tsv`, `src/vk.py` `TOKENS`): Tomokiyo's symbols with names; additions are marked in `TOKENS` (source `C` = from the calibration page, otherwise `T` = Tomokiyo). See OPEN.md §1 for symbols not in his table.
2. **First transcription** (`data/transcription/<page>_first.txt`): p.33 and p.539 by Claude Opus; the other pages by Claude Sonnet, from enlarged tiles. Symbol names, one row per manuscript line.
3. **Second transcription for checking** (`second/<page>_pass1.txt`): OpenAI Codex CLI (codex-cli 0.163.0-alpha.10.2, default model — the run log does not name it), one run per page, `codex exec --ephemeral -s read-only` from an empty folder, given only the line images (cut by `src/lines.py`) and `second/PROMPT.md` (symbol names and shape descriptions; no values, no key, no first reading). Run logs show one reply and no command or file access. (`second/p525_pass1_misaligned.txt` is a first run of p.525 whose line images were shifted by two lines; it was rerun and is kept only for the record.)
4. **Image adjudication** (`xcheck/adjudication_img_<page>.tsv`, `xcheck/ADJUDICATE_PROMPT.md`): Claude Sonnet looked at each disagreement between 2 and 3 in enlarged crops and changed the first reading only when the image clearly supported the other; otherwise it kept the first reading and marked it "?". The result is the final transcription `data/transcription/<page>.txt`.
   - Where an image-based change produced non-words in a systematic way (p→φ "mait/maire", 3→ʒ "serblable", qa→al "auon"), the main session put the first reading back and marked it "?" (p.525: 11 symbols; p.526: 3; p.561: 1). These are context decisions, not image decisions, and are counted as undecided.
   - Counts of adjudicated disagreements (rows in the TSVs; one row may span several symbols):

     | page | rows | kept first | took second | ambiguous (kept, "?") |
     |---|---|---|---|---|
     | p.33 | 38 | 18 | 2 | 18 |
     | p.525 | 115 | 46 | 59 (11 reverted by context, see above) | 10 |
     | p.526 | 89 (9 formatting only) | 25 | 16 (+5 mixed) | 34 |
     | p.539 | 36 (5 formatting only) | 12 | 1 (+2 mixed) | 16 |
     | p.561 | 96 | 54 | 16 | 26 |
     | p.562 | 43 | 35 | 5 | 3 |
     | p.563 | 93 | 49 | 5 | 39 |
     | p.565 | 103 | 63 | 12 | 28 |
     | p.570 | 5 | 1 | 0 | 4 |
5. **Independent second transcription** (`second/<page>_pass2.txt`): Codex again, new context, same prompt and images, after the final transcription was fixed. This is the comparison reported as "independent" (step 3 was used to correct the first reading and is therefore not independent).
6. **Decoding** (`src/vk.py decode` → `data/decoded/`) and word division by hand (Claude Opus) in `docs/READING*.md`.
7. **Control**: the letter values of the key were shuffled among the letter symbols 1,000 times; each shuffled key and the real key were scored on runs of single-letter symbols by a character-trigram model of French (wordfreq, top 50,000 words; j→i, v→u). `src/vk.py control`.
8. **Calibration**: Codex's transcription (made without the margin; the margin was cut away from the line images) of two pages that have a contemporary decipherment (p.33 and p.258) was decoded with the key and compared letter by letter with the margin (`src/calib.py`). The margin of p.258 was transcribed by Claude Sonnet without looking at the cipher; the margin of p.33 by Claude Opus.

## Numbers
**Independent second transcription** (final transcription vs Codex pass 2, letters compared after mapping symbols to values, per line, `src/xcompare.py`):

| p.33 | p.525 | p.526 | p.539 | p.561 | p.562 | p.563 | p.565 | p.570 | total |
|---|---|---|---|---|---|---|---|---|---|
| 93.8% | 86.3% | 84.6% | 85.9% | 81.5% | 87.3% | 87.3% | 91.7% | 73.1% | **4,017/4,637 = 86.6%** |

Counted by symbol name instead of value (Codex often gives a different name to the same shape, e.g. oc as fl): 3,996/4,661 = 85.7% (p.561 81.1%, p.570 73.1%, others 83–92%).

For comparison: Codex pass 1 vs Codex pass 2 (the same model reading the same images twice) 90.9%; first transcription (before adjudication) vs Codex pass 1 86.7%; first transcription vs Codex pass 2 84.9%. Most disagreements are between look-alike pairs (OPEN.md §2).

**Control** (`xcheck/control_v2.tsv`, 1,000 shuffles each; "table only" = only symbols in Tomokiyo's table):

| page | symbols scored | real key | best shuffled | shuffled ≥ real | table only: shuffled ≥ real |
|---|---|---|---|---|---|
| p.33 | 242 | −1.806 | −3.483 | 0 | 0 |
| p.525 | 879 | −2.820 | −4.533 | 0 | 0 |
| p.526 | 515 | −2.972 | −4.406 | 0 | 0 |
| p.539 | 173 | −2.041 | −3.849 | 0 | 0 |
| p.561 | 706 | −3.168 | −4.409 | 0 | 0 |
| p.562 | 810 | −2.914 | −4.311 | 0 | 0 |
| p.563 | 528 | −2.998 | −4.403 | 0 | 0 |
| p.565 | 534 | −2.926 | −4.334 | 0 | 0 |
| p.570 | 23 | −3.507 | −3.532 | 0 | 1 |

Applying the key unchanged to Codex's own transcriptions also gives 0/1,000 on every page (p.33, p.525–565).

**Calibration** (Codex transcription → key → compared with the contemporary margin; letters only; long gaps ≥4 letters — code-word positions and text outside the margin's span — are not scored):

| page | letters scored | agree | not scored |
|---|---|---|---|
| p.33 | 234 | 200 (85.5%) | 72 |
| p.258 | 389 | 319 (82.0%; 83.5% if d and l are merged) | 461 |

Counting all margin letters instead (runs of ≥4 matching letters), 42% of the p.258 margin is matched; the difference is mostly code words (the margin spells out "l'Electeur palatin", "les autres electeurs", etc. where the cipher has plain-letter code groups) and Codex's reading of 9 as q (d→l).

**Share of symbols with a value**: of 4,667 symbols and plain-letter groups in the final transcription, 4,551 (97.5%) are symbols with a value, 20 (0.4%) are unreadable, and 96 (2.1%) are plain-letter groups (code words or nulls), most without a known meaning.

**Level (thresholds used for this series of repositories)**: B, "partial reading" — control 0/1,000 on every page, independent agreement ≥70% on every page (lowest p.570, 73.1%), calibration ≥65%. Not C ("full reading"): independent agreement is below 85% on p.526, p.561 and p.570, and calibration on p.258 is 82.0% (letters).

## AI use (COPE disclosure)
- Claude Opus 5.5 (main session, Claude Code): prior-work search, key table, first transcription of p.33 and p.539, orchestration, decoding, word division of the readings, documents. It reverted 15 image-adjudication changes by context (marked "?").
- Claude Sonnet 5.5 (sub-agents): first transcription of p.525–526, 561–565, 570; image adjudication of all disagreements; transcription of the p.258 margin; search for code-word meanings in the deciphered letters (mostly unsuccessful).
- OpenAI Codex CLI 0.163.0-alpha.10.2 (default model): second transcriptions (pass 1 used for adjudication, pass 2 independent) and the calibration transcription of p.258.
- No human has checked the transcriptions, the adjudication, or the readings against the manuscript. Agreement between AI systems is not a substitute for a human check.

## Limits
- Look-alike symbol pairs (OPEN.md §2) are decided partly by context; uppercase letters in the key output show the uncertain ones.
- Code words are mostly unexplained (OPEN.md §3); the readings put them in [brackets].
- Calibration covers two pages and uses AI transcriptions of the margins.
- p.570 has only one line (23 symbols); its control result is weak.
