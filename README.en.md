# Ancel's cipher letters in BnF Colbert 398 (Oct–Dec 1577): reading of the passages left undeciphered

[日本語の README](README.md)

BnF, Cinq Cents de Colbert 398 holds letters of Jean de Vulcob (1575–76) and Guillaume Ancel (1576–78, 1584), French residents at the Imperial court. Most cipher passages carry a contemporary decipherment in the left margin. This repository reads the passages that have none (p.525–526, p.539, p.561–563, p.565 and one line on p.570) with Satoshi Tomokiyo's reconstructed key "Vulcob and Ancel's Cipher (1575-1584)".

- **Status: partial reading.** 125 cipher lines (4,377 symbols) are read through and most read as words ([docs/READING.en.md](docs/READING.en.md)). Most code words (plain-letter groups inside the cipher) are unexplained, and some look-alike symbol pairs are decided by context ([docs/OPEN.en.md](docs/OPEN.en.md)).
- **Relation to prior work:** the key is Tomokiyo's reconstruction; he writes that it "will allow reading undeciphered letters" ([Cryptiana, French Ciphers for German (and Eastern) Affairs](https://cryptiana.web.fc2.com/code/frencheastern.htm)) but publishes no readings. George Lasry compared a key in this volume when he deciphered the 1573 letter to Vulcob (BnF fr.3318; [Cryptiana GL.htm](https://cryptiana.web.fc2.com/code/GL.htm)). In the places searched we found no published reading of these pages (SOURCES.md, 20 Oct 2026). A separate adversarial prior-work check has not yet been done, so we do not claim to be first. Damien Fontvieille gave a conference paper on Vulcob's ciphered correspondence in 2024; its content could not be checked.
- **No human has checked the transcription.** Transcription, cross-checking and reading are by AI (Claude and OpenAI Codex) and have not been checked by a person against the manuscript. Agreement between AI systems is not a substitute for a human check.
- **Numbers** (sources in [docs/METHOD.en.md](docs/METHOD.en.md)):
  - Independent second transcription: after the transcription was fixed, OpenAI Codex read the line images again in a new context, given only the images and the list of symbol names. Agreement by value 4,017/4,637 = 86.6% (73.1–93.8% per page; 85.7% by name). Codex agrees with itself on two readings of the same images 90.9%.
  - Control: 1,000 keys with shuffled letter values; none scores as well as the real key on any page.
  - Calibration: on two pages that have a contemporary decipherment (p.33, p.258), Codex's transcription made without the margin, decoded with the key, agrees with the margin on 85.5% (234 letters) and 82.0% (389 letters) of the letters compared; long gaps (code-word positions etc.) are not scored.
  - 97.5% of symbols have a value, 0.4% are unreadable, 2.1% are plain-letter groups.
- **AI use:** prior-work search, key table, transcription, decoding, scripts and documents by Anthropic's Claude (Claude Code; mainly Claude Opus 5.5, with Claude Sonnet 5.5 for part of the transcription and the image adjudication). Second transcriptions (for cross-checking, and the independent one) by OpenAI Codex (codex-cli 0.163.0-alpha.10.2, default model). Choice of target, direction of the work and the decision to publish by a human.

## Content (summary; includes inference)
- **22 October 1577 (p.523–526):** Archduke Matthias's departure for the Low Countries. Malstet, envoy of the States, had asked the Emperor for Matthias "not as governor but as lord". The cipher gives Ancel's view that the Emperor (code word *saturnus*) will deny any part in it, and why: the young archduke could not take a step out of his room without his brother's leave, could not have left the castle that is shut at night, and had no one to rely on.
- **2 November 1577 (p.539):** the Emperor does all he can to persuade the Spaniards that the departure happened without his knowledge.
- **14 December 1577 (p.561–563):** the Marquis of Varambon, sent by Don John of Austria to obtain leave to levy troops in Germany, has waited more than three weeks for an answer; the Spanish envoy Borgia says that if the Emperor supports his brother he must do it in earnest, as the Catholic King will do everything to keep his right; the Emperor gives the Spaniards fair words but secretly does things against them; the Estates of the Empire will hardly grant extraordinary aid.
- **21 December 1577 (p.565):** Varambon is back from Archduke Charles's court and has obtained nothing; the Emperor waits for the answer of the King of Spain (code word *Juno*, inferred) to what he wrote after Matthias's departure.

## What this work adds
1. Identification of the passages without a contemporary decipherment (all pages listed by Tomokiyo were viewed; docs/METHOD.en.md).
2. A line-by-line transcription of those passages in symbol names (`data/transcription/`).
3. Additions and checks to the key: uu, ff, nn; the flat L-like sign = g; a lone c = null; etc. (docs/OPEN.en.md §1).
4. The reading, controls, calibration and an independent second transcription by another AI.

## Layout
| path | content |
|---|---|
| docs/READING*.md | key output and reading per line |
| docs/METHOD*.md | method, numbers, AI use, limits |
| docs/OPEN*.md | open points (symbols, code words, unread passages) |
| data/key.tsv | key table (Tomokiyo's table in symbol names) |
| data/transcription/ | final transcription (`<page>.txt`) and first pass (`<page>_first.txt`) |
| data/decoded/ | key output |
| second/ | Codex transcriptions (pass1 = cross-check, pass2 = independent) and the prompt |
| xcheck/ | image adjudication records, comparison with the independent pass, control table |
| calib/ | calibration (margin transcriptions, key output on Codex's reading) |
| src/ | key and control (vk.py), comparison (xcompare.py), calibration (calib.py), line cutting (lines.py, tiles.py) |
| tests/ | `python3 -m unittest discover -s tests` |

No images are included. Sources are cited by shelfmark and Gallica view number in SOURCES.md.

## Change log
- 2026-10-20: first version.
