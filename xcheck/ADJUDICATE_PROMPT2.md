# Prompt used for the second image adjudication (file names adapted to this repository: <page>_before.txt = data/transcription/intermediate/<page>.txt, <page>_after.txt = data/transcription/<page>.txt)

Image-based adjudication a second time of a 16th-century French symbol-cipher transcription (BnF Cinq Cents de Colbert 398). Paleography only.

For each page assigned to you :
- Current transcription: transcription/<page>_before.txt (symbol names, one row per manuscript line).
- Line images: xcheck/img/<page>/<page>_LNN.jpg (LNN = line NN of the transcription; for p033 the rows are 33.01–33.08 = L01–L08). Crop and enlarge with Python/PIL in a temporary folder OUTSIDE the project (e.g. /tmp/adj3_<page>).
- Three independent transcriptions by another AI (Codex), in symbol names: second/<page>_pass3a.txt, _pass3b.txt, _pass3c.txt; their value-level majority: second/<page>_pass3vote.txt. The per-line disagreements (current > majority, in VALUE space) are column 6 of xcheck/compare_<page>_before_pass3vote.tsv. Name → value: work/vk.py TOKENS. Shape descriptions: xcheck/PROMPT2.md. Key table image: src/vulcob_key_x3.png.
- Do NOT open calib/, decoded*/, READING.md, DECIPHERMENT.md or gallica/; do not use what the text "should" say.

Task: for each disagreement, look at the image and change the current transcription ONLY when the image clearly shows the other reading. Decide from the SHAPE (∂ short with hooked head = i vs δ tall with arching ascender = dl; 9 short curved tail vs q long straight stem; oc = cross with a small loop/triangle BELOW the bar vs 4 = closed triangle ABOVE-left of the bar; large-arc S; L flat vs g tall; etc.). If the image is not clear, keep the current reading and append "?" if not already there. For the look-alike pairs 3/ʒ(z), p/φ(phi) and qa/al never change on shape alone (keep current + "?"). Missing or extra symbols: add/delete only if you can see the symbol is there/absent.

Write transcription/<page>_after.txt (copy of _before with your changes; keep all header lines and add "# adjudicated by image a second time against three independent Codex readings, <date>") and xcheck/adjudication2_img_<page>.tsv with columns: line, position/context, current, other, decision (current/other/ambiguous), reason (what you saw). Report per page: disagreements examined, kept current, took other, ambiguous, and any systematic finding. Write no other files in the project.
