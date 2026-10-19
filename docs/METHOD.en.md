# Method, numbers, AI use and limits

Japanese: METHOD.md

## Material
- BnF, Cinq Cents de Colbert 398 (Gallica ark:/12148/btv1b525218133): original letters to Charles IX, Henry III and Catherine de Médicis on the affairs of Germany, including dispatches of Jean de Vulcob (1575–76) and Guillaume Ancel (1576–78, 1584), French residents at the Imperial court. Page numbers are the manuscript pagination; "f" numbers are Gallica views (page→view table in SOURCES.md).
- Key: S. Tomokiyo's reconstruction "Vulcob and Ancel's Cipher (1575–1584)" (Cryptiana, `code/frencheastern.htm`, image `easternVulcob.png`; page Last-Modified 15 Mar 2026). Tomokiyo lists the letters and writes that the key "will allow reading undeciphered letters"; he publishes no readings of them.
- Images: BnF IIIF Image API, 2400 px wide. No image is included here.

## Which passages were undeciphered
All cipher pages listed by Tomokiyo were viewed. Most carry a contemporary decipherment in the left margin. The cipher on p.525–526, p.539, p.561–563, p.565 and the single cipher line on p.570 has none; these are read here (125 cipher lines, 4,377 symbols in the final transcription).

## Steps
1. **Key table** (`data/key.tsv`, `src/vk.py` `TOKENS`): Tomokiyo's symbols with names; additions are marked in `TOKENS` (source `C`), the rest is his table (`T`). Symbols not in his table: OPEN.en.md section 1.
2. **First transcription** (`data/transcription/<page>_first.txt`): p.33 and p.539 by Claude Opus 5.5, the other pages by Claude Sonnet 5.5, from enlarged tiles, in symbol names, one row per manuscript line.
3. **Cross-check transcription** (`second/<page>_pass1.txt`): OpenAI Codex CLI (codex-cli 0.163.0-alpha.10.2, default model; the run log does not name the model), one run per page, `codex exec --ephemeral -s read-only` from an empty folder, given only the line images (cut by `src/lines.py`, one `-i` per image) and `second/PROMPT.md` (symbol names and shape descriptions; no values, no key, no first reading). The prompt was sent on standard input. The run logs contain one reply and no command execution. (`second/p525_pass1_misaligned.txt` is a first run of p.525 whose line images were shifted by two lines; it was rerun and is kept only for the record.)
4. **Image adjudication** (`xcheck/adjudication_img_<page>.tsv`, prompt in `xcheck/ADJUDICATE_PROMPT.md`): Claude Sonnet 5.5 looked at each disagreement between 2 and 3 in enlarged crops and changed the first reading only when the image clearly showed the other; otherwise it kept the first reading and marked it "?". Result: the final transcription `data/transcription/<page>.txt`.
   - In three places an image-based change made non-words in a systematic way (p→φ "mait, maire"; 3→ʒ "serblable, directerent"; qa→al "auon"). Claude Opus 5.5 put the first reading back and marked it "?" (p.525: 11 symbols; p.526: 3; p.561: 1). These 15 are decided by context, not by the image, and are counted as undecided.
   - Rows in the adjudication tables (a row may span several symbols): p.33 38 (kept first 18 / took second 2 / undecided 18); p.525 115 (46 / 59, of which 11 later reverted by context / 10); p.526 89, 9 formatting only (25 / 16, +5 mixed / 34); p.539 36, 5 formatting only (12 / 1, +2 mixed / 16); p.561 96 (54 / 16 / 26); p.562 43 (35 / 5 / 3); p.563 93 (49 / 5 / 39); p.565 103 (63 / 12 / 28); p.570 5 (1 / 0 / 4).
5. **Independent second transcriptions** (made after the final transcription was fixed, never shown it): Codex, new context each time, the same line images.
   - pass 2 (`second/<page>_pass2.txt`): prompt `second/PROMPT.md`, one run.
   - pass 3a, 3b, 3c (`second/<page>_pass3[abc].txt`): prompt `second/PROMPT2.md`, which describes more precisely the look-alike shapes found during adjudication (9/q, ∂/δ, the cross signs, the large-arc S, qa/al, L/g). Three separate runs. `src/vote.py` makes a value-level majority of the three without using our transcription (`second/<page>_pass3vote.txt`), reported for information only.
6. **Reading**: `src/vk.py decode` (→ `data/decoded/`), word division by Claude Opus 5.5 (`docs/READING*.md`).
7. **Control**: the letter values of the key shuffled among the letter symbols 1,000 times; each shuffled key and the real key scored on runs of single-letter symbols by a character-trigram model of French (wordfreq, top 50,000 words; j→i, v→u). `src/vk.py control`.
8. **Calibration**: p.258, a page with a contemporary decipherment in the margin, was processed exactly like the undeciphered pages without the margin being seen: line images without the margin; first transcription by Claude Sonnet 5.5 (`calib/p258_first.txt`); disagreements with the majority of three Codex runs adjudicated by image (`calib/p258.txt`, `xcheck/adjudication_img_p258.tsv`); key applied (`calib/p258_decode.tsv`). The margin was transcribed separately by Claude Sonnet 5.5 and by Codex, and the differences adjudicated by image (`calib/p258_margin_adj.txt`, log `calib/p258_margin_adj_log.tsv`). The decode was compared letter by letter with the adjudicated margin (`src/calib.py`).

## Numbers
**Independent second transcription** (final transcription vs each independent run; symbols mapped to values, aligned per line, `src/xcompare.py`). The lowest run is the one that counts.

| run | p.33 | p.525 | p.526 | p.539 | p.561 | p.562 | p.563 | p.565 | p.570 | total |
|---|---|---|---|---|---|---|---|---|---|---|
| pass 2 | 93.8% | 86.3% | 84.6% | 85.9% | 81.5% | 87.3% | 87.3% | 91.7% | 73.1% | 4,017/4,637 = 86.6% |
| pass 3a | 93.5% | 97.8% | 87.8% | 99.0% | 97.6% | 95.4% | 93.7% | 93.8% | 84.6% | 4,402/4,637 = 94.9% |
| pass 3b | 88.1% | 97.8% | 87.6% | 95.8% | 97.4% | 95.7% | 94.3% | 92.7% | 88.5% | 4,380/4,637 = 94.5% |
| pass 3c | 88.8% | 97.7% | 87.6% | 98.4% | 96.9% | 95.9% | 93.9% | 94.5% | 88.5% | 4,392/4,637 = 94.7% |
| **lowest** | 88.1% | 86.3% | **84.6%** | 85.9% | **81.5%** | 87.3% | 87.3% | 91.7% | **73.1%** | |

By symbol name instead of value (`src/namecompare.py`): pass 2 84.7%, pass 3a 92.4%, pass 3b 91.9%, pass 3c 92.0% (lowest page: p.570, 73.1% in pass 2). For information: majority of 3a–3c 95.2%; Codex pass 1 vs pass 2 (same model, same images, same prompt) 90.9%; first transcription before adjudication vs pass 1 86.7%.

**Control** (`xcheck/control.tsv`, 1,000 shuffles each; "table only" = only symbols in Tomokiyo's table):

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

Applying the key unchanged to Codex's own transcriptions (pass 1) also gives 0/1,000 on p.33 and p.525–565.

**Calibration** (letters only; long gaps of ≥4 letters — code-word positions and text outside the margin's span — are not scored):

| what is compared | letters scored | agree |
|---|---|---|
| **p.258, full procedure** (adjudicated transcription → key) vs adjudicated margin | 412 | **333 (80.8%)** |
| same, d and l merged | 379 | 309 (81.5%) |
| p.258, first transcription only → key vs adjudicated margin | 376 | 304 (80.9%) |
| p.258, Codex pass 1 → key vs margin (Sonnet's reading) | 389 | 319 (82.0%) |
| p.33, Codex pass 1 → key vs margin (read by Claude Opus 5.5) | 234 | 200 (85.5%) |

The full-procedure figure against the adjudicated margin (80.8%) is the one that counts. Against the other margin readings the same decode gives 82.1% (Sonnet) and 85.8% (Codex); the spread shows that the reference itself is uncertain. Many letters are not scored (430 on p.258), mostly where the margin spells out what the cipher gives as a plain-letter code word.

**Share of symbols with a value**: of 4,667 symbols and plain-letter groups in the final transcription, 4,551 (97.5%) are symbols with a value, 20 (0.4%) are unreadable, and 96 (2.1%) are plain-letter groups (code words or nulls), most without a known meaning.

**Status: partial reading.** Control 0/1,000 on every page; independent agreement at least 73.1% on every page in every run; calibration 80.8%. Not called a full reading because the lowest independent agreement is below 85% on p.526 (84.6%), p.561 (81.5%) and p.570 (73.1%, one line), the calibration is below 85%, and most code words are unexplained.

## AI use (COPE disclosure)
- Claude Opus 5.5 (Anthropic): prior-work search, key table, first transcription of p.33 and p.539, coordination, decoding, word division, the 15 context reversions, documents.
- Claude Sonnet 5.5 (Anthropic): first transcription of p.525–526, 561–565, 570 and of the calibration page p.258; image adjudication of all disagreements; transcription and adjudication of the p.258 margin; search for code-word meanings in the deciphered letters (mostly unsuccessful).
- OpenAI Codex CLI 0.163.0-alpha.10.2 (default model): cross-check transcription (pass 1), independent transcriptions (pass 2, pass 3a–c), a transcription of the p.258 margin.
- A separate Claude reader that took no part in the decipherment searched for prior work (docs/PRIOR_CHECK.en.md).
- **No human has checked the transcriptions, the adjudication or the readings against the manuscript.** Agreement between AI systems is not a substitute for a human check.

## Limits
- Look-alike symbol pairs (OPEN.en.md section 2) are decided partly by context; uppercase letters in the key output mark the uncertain ones.
- Code words are mostly unexplained (OPEN.en.md section 3); the readings put them in [brackets].
- Calibration rests on one page and on AI readings of its margin.
- p.570 has one line (23 symbols scored); its control result is weak.
