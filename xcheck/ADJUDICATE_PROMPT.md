# Prompt used for the image adjudication (file names adapted to this repository: <page>_adjudicated.txt = data/transcription/<page>.txt)

Image-based adjudication of two independent transcriptions of a 16th-century French symbol-cipher letter (BnF Cinq Cents de Colbert 398). Paleography only.

For each page assigned to you:
- Line images (one per cipher line, in order): xcheck/img/<page>/<page>_LNN.jpg  (LNN = line NN of the first transcription, e.g. p525_L03 = 525.03).
- First transcription (symbol names, one row per line): transcription/<page>.txt
- Second, independent transcription by another AI (Codex), same symbol names but it sometimes uses different names for the same shape: xcheck/out/<page>_pass1.txt
- Disagreement list in VALUE space (first>second), per line: xcheck/compare_<page>.tsv (column 6). Values come from work/vk.py TOKENS (name -> letter).
- Shape references: src/vulcob_key_x3.png (key table), key.tsv, xcheck/PROMPT.md (shape descriptions the second transcriber used).
(in this repository: transcription/ = data/transcription/, xcheck/out/ = second/)

Task: for every disagreement, look at the line image (crop and enlarge with Python/PIL), decide which reading the image supports, and write a corrected copy of the first transcription as transcription/<page>_adjudicated.txt (same format and line ids; keep the header lines and add "# adjudicated by image against Codex pass1, <date>"). Change a token only when the image clearly supports the other reading; if the image is genuinely ambiguous, keep the first reading and append "?" to the token. Pay special attention to: ∂ (i, hook curling up-left) vs δ (dl, tall upright loop); 9 (d, short tail) vs q (l, long tail); the circled hook S vs other signs; 3 (m) vs ʒ (z, r); ⊤-with-loop oc (o) vs t4 vs 4 (a); qa vs al. Decide from the SHAPE, not from what makes good French.

Also write xcheck/adjudication_img_<page>.tsv with columns: line<TAB>position/context<TAB>first_token<TAB>second_token<TAB>decision(first/second/ambiguous)<TAB>short reason (what you saw).

Report per page: number of disagreements examined, kept first, took second, marked ambiguous; and any systematic finding (e.g. "the second transcriber calls oc 'fl' throughout"). Write no other files in the project.
