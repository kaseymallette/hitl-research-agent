# Close-reading judgment

**Article:** `article.pdf` — Alissa, H. et al. "Using life cycle assessment to drive
innovation for sustainable cool clouds." *Nature* 641, 331–338 (2025).

**Run judged:** `run/analysis.json` (26 steps, 164 claims, 74 support items, 72 citations).

**Seed (A1 sample):** `20261106`, Python 3.14 `random.seed(20261106)`, then
`random.sample` of 30 from the 164 claims listed in reading order as (step, claim) pairs.

**Sources used:** `RUBRIC.md`, `article.pdf` (text extracted with pypdf; Fig. 4 and
Extended Data Table 1 rendered and checked by eye), `references/claims_reference.md`
(used as written), `run/analysis.json`.

**Note on the instructions:** `prompts/close-reading.md` isn't in the folder. Only
`prompts/evaluate-argument.md` is there, and I didn't open it because it belongs to the
other session. So the run is judged against the close-reading requirements that
`RUBRIC.md` sets out: keep the author's strength of language, mark `verbatim` only for
exact wording, mark readings of images as `paraphrased` and name the element, and never
invent a reference. Instructions in the missing file that the rubric doesn't repeat
couldn't be checked.

Claim IDs below are `C<step>.<claim>` (zero-based, in file order). Support items are
`.S<n>`.

---

## A1. Attribution fidelity

Sample: C0.0, C0.1, C0.2, C1.1, C2.0, C2.6, C2.7, C3.2, C4.4, C5.4, C5.5, C6.4, C7.5,
C8.0, C8.4, C8.5, C9.0, C10.2, C10.4, C12.0, C12.4, C13.2, C14.9, C18.6, C19.3, C19.4,
C20.1, C24.2, C25.0, C25.2. These 30 claims carry 14 support items.

| Score | Claims (n = 30) | Support items (n = 14) |
| --- | --- | --- |
| 2 | 30 (100%) | 14 (100%) |
| 1 | 0 (0%) | 0 (0%) |
| 0 | 0 (0%) | 0 (0%) |

Every passage was found. There were no cases I couldn't locate.

| Claim | Form | Passage | Score | Note |
| --- | --- | --- | --- | --- |
| C0.0 | para | standfirst, p.331 | 2 | AB-1. S0 (ref. 1, DOE) is the citation on "data centres and cloud" — 2. |
| C0.1 | verb | standfirst | 2 | Exact. The superscript 2 is left out of the claim text and shown as the citation. S0 (ref. 2, ISO 14040) — 2. |
| C0.2 | para | standfirst | 2 | Combines AB-2 ("from virtual machines … to the grid") with AB-4 (software/chips/servers/buildings, "adoption guidelines"). The scope is kept. |
| C1.1 | para | p.331 | 2 | Same list of applications. "Driving the rapid acceleration and transfer" is kept. S0 (refs 3–5) — 2. |
| C2.0 | verb | p.331 | 2 | Exact. |
| C2.6 | para | pp.331–332 | 2 | Three technologies, efficiency/performance, and the life-cycle stages, all as stated. |
| C2.7 | para | p.332 | 2 | Keeps "to our knowledge", "first public" and "hyperscale cloud provider". S0 matches "extensively reviewed13,14" — 2. |
| C3.2 | para | p.332 | 2 | Keeps "will probably push". S0 describes refs 16–17 from their titles — 2. |
| C4.4 | para | p.332 | 2 | "Natural and/or forced convection", "usually hydrocarbon … sometimes fluorinated". It drops the parenthesis "(but on a smaller scale than for two-phase immersion)", but the claim's force doesn't change. S0 reads Fig. 1b and its caption (mineral oil, ref. 25) correctly — 2. |
| C5.4 | para | p.333 | 2 | The causal chain to TCO and embodied carbon is as written. |
| C5.5 | para | p.333 | 2 | S0 (Intel retrofit, ref. 22) — 2. |
| C6.4 | para | p.333 | 2 | LHV, non-renewable, MJ. |
| C7.5 | para | p.333 | 2 | 2021 US grid, coal 22%, gas 38%. S0 (ref. 35, EIA) — 2. |
| C8.0 | para | p.334 | 2 | PG25, 75:25, spent-glycol EOL. |
| C8.4 | para | Table 3 | 2 | All values match: +3/6/6% MW, +20/10/20% overclocking, −3/6/6% PUE and server power, +28/25/36% Vcores. |
| C8.5 | para | Table 3 | 2 | Identical IT shares. Server counts +6/13/13% and +10/13/13%. |
| C9.0 | verb | p.334 | 2 | Exact. |
| C10.2 | para | p.335 | 2 | "Low compared with other components". S0 reads Fig. 4 fluid segments as small and says no segment values are printed. Correct by eye — 2. |
| C10.4 | para | p.335 | 2 | Keeps "are possible" and the four conditions on choice. S0 (water-stressed regions) — 2. |
| C12.0 | para | p.336 | 2 | "Highlights the need for improved … data" becomes "making better server component data necessary". The strength is the same. S0 (Fig. 4 renewable GHG bars mostly server) checked by eye — 2. S1 (ref. 41) — 2. |
| C12.4 | para | Table 4 footnote | 2 | Keeps "not suggesting any of them are superior" and the sensitivity hedge. S0 reads footnotes a–c, including "tends to" and "will mostly depend" — 2. |
| C13.2 | para | p.336 | 2 | "Most notable" becomes "largest" and "provides opportunities to engage" becomes "helps … engage". Both are close. "Ensure a harmonized approach to advancing potentially sustainable technologies" is kept. |
| C14.9 | verb | p.337 | 2 | Exact. |
| C18.6 | para | PDF p.9–10 | 2 | Keeps "conservatively", 16-layer PCB, and the one-third/two-thirds split. |
| C19.3 | para | PDF p.10 | 2 | Order of data sources and the three proxies are as listed. |
| C19.4 | para | PDF p.10 | 2 | Water use substituted for consumption. LCA FE water proxy. |
| C20.1 | para | PDF p.10 | 2 | PUE and load-factor definitions. "Conservative assumption for the utilization rate" is kept. |
| C24.2 | verb | PDF p.12 | 2 | Exact (Competing interests). |
| C25.0 | para | Ext. Data Table 1 (image) | 2 | Reliability scale 1–5 matches the image. Correctly `paraphrased`, with the table named. S0 ("Adapted from ref. 51") — 2. |
| C25.2 | para | Ext. Data Table 1 (image) | 2 | <3, <6, <10, <15 years, and unknown or >15. Matches the image. |

**Outside the sample (not scored, recorded for A3):** C1.6 says "The authors say ICT must
reduce sector GHG emissions 42% by 2030". In the article, this "must" belongs to SBTi
("SBTi indicates that a 42% reduction … must occur"). The authors' own normative claim is
weaker: the sector "should prioritize" such designs. The claim's support item does name
SBTi, so the source is recoverable, but the claim text puts SBTi's wording in the
authors' mouth. If sampled, I would score it 1.

## A2. Coverage

Counted against `claims_reference.md`. The reading runs to PDF p.13, the end of the
article, so it covers the whole span the list covers (main text, Methods, Extended Data
Table 1).

| Type | In list | Caught | Caught without what it shows | Missed |
| --- | --- | --- | --- | --- |
| Abstract claims | 6 | 6 | 0 | 0 |
| Contributions | 9 | 9 | 0 | 0 |
| Conclusions, main text (section/subsection units) | 11 | 11 | 0 | 0 |
| Conclusions, Methods (units) | 9 | 9 | 0 | 0 |
| Figures | 4 | 4 | 0 | 0 |
| Tables | 5 | 5 | 0 | 0 |

Where each item is caught:

- **Abstract:** AB-1 C0.0. AB-2 and AB-4 combined in C0.2. AB-3 C0.1. AB-5 C0.3. AB-6 C0.4.
- **Contributions:** C-1/C-2 C2.7. C-3 C6.1. C-4 C0.3 plus step 5 (C5.8, and moves
  "restating the purpose and headline results"; the p.333 repetition of the 15–21% figures
  isn't a separate claim). C-5 C7.2 and C15.3. C-6 C9.0 with C7.8. C-7 C15.1. C-8 C16.2 S0.
  C-9 C24.0.
- **Main-text conclusions:** S-1 steps 1–2. S-2 step 3. S-3 steps 4–5. S-4.1 step 6.
  S-4.2 steps 7–8. S-4.3 C8.3. S-5 steps 9–10 (S-5a–h each has a claim). S-6 steps 11–12.
  S-7 steps 13–14. S-8 step 15 (C15.0, C15.1, C15.3 with the 10 GW example). S-9 step 16.
- **Methods:** M-1a–d step 17. M-1e C18.0–18.2. M-1f C18.3–18.7. M-1g C19.0–19.1.
  M-1h C19.2–19.5. M-2 step 20. M-3 step 21, with the one-phase fluid chain and the
  two-phase confidentiality recorded earlier at C8.1–8.2. M-4 step 22. M-5 step 23.
- **Figures:** F-1 is read panel by panel in C4.2.S0, C4.4.S0 and C4.5.S0. F-2 in C5.6.S1.
  F-3 in C6.6.S0. F-4 in C11.6.S0, with all 24 printed totals, each correct against the
  image. F-4 segment readings appear in C9.3.S0, C10.2.S0 and C12.0.S0.
- **Tables:** T-1 cell by cell in C5.0–5.2 S0. T-2 C7.4. T-3 C8.4–8.5. T-4 C9.1.S0,
  C11.3.S0 and C12.4 with its footnotes. T-ED1 C25.0–25.4.

**Partial points (not counted as misses):** the Methods restatement of the grid mix and
EOL basis (M-1b) has no claim of its own in step 17. The reading already recorded it at
C7.5–C7.7. The M-5a/S-7g wording difference ("most efficient" vs "all … offer efficient")
is recorded verbatim on both sides (C14.9 and C23.0) but not flagged. The reading wasn't
asked to flag it.

**Found beyond the list** (confirmed in the article; the list stays as it is):

- C14.0: one-phase hydrocarbon oils "recognized for their dielectric properties, low
  toxicity and low fluid loss" (p.336). The list records only the cons.
- C14.2: clean-up after total fluid loss to ground by replacing contaminated soil
  (p.336).
- C17.1: services such as Microsoft 365, used to ground the Vcore (PDF p.9).
- C24.1 and C24.2: author contributions and the competing-interests statement ("The
  authors are/were employees of Microsoft or WSP"), PDF p.12. The list deliberately
  leaves these out. They are confirmed in the article and relevant to provenance.

## A3. Strength of language — **2**

Conditions, samples, scope, units and hedges survive throughout. In the sample and the
wider read:

- Kept: "will probably push" (C3.2), "to our knowledge" (C2.7), "were found to be an ideal
  comparison unit" (C7.2), "could have … but might involve" (C13.4), "may not have as low
  PUE" (C13.3), "are possible" (C10.4), "conservatively modelled" (C18.6), "may be
  effective" (C23.2), and "potential barrier" rendered as "may impede" (C23.1).
- Self-assessments are attributed as the authors': "the authors judge variability
  manageable and overall uncertainty low" (C22.4).
- The Table 4 disclaimer ("not suggesting any of them are superior") is carried in C12.4.
- Every number keeps its unit and case. Grid and renewable savings are kept apart
  (C9.1, C11.3). Supply-switch deltas are labelled as normalized to air cooling
  (C11.6). The Fig. 4 index is explained as a remaining impact, not a saving (step 11
  meaning).
- Strong author language isn't softened: "will lead to marked reductions" (C13.0),
  "excellent potential" (C15.0), "transformative potential" (C0.4) are all verbatim.

The one shift found is C1.6 (SBTi's "must" given to the authors; see A1). Small
lexical substitutions such as "most notable" to "largest" (C13.2) don't change strength.
One instance doesn't make a pattern in either direction.

## A4. Mechanical checks

Checked by script against the pypdf extraction of `article.pdf`. Whitespace and PDF
hyphenation were normalized, and superscript citation numbers were ignored.

| Check | Pass | Fail | Notes |
| --- | --- | --- | --- |
| Verbatim texts found in the article | 19 | 0 | All 19 are claims; no support item is marked verbatim. C0.1, C6.0 and C15.0 match once printed superscript citations (2, 2,12, 44) are dropped. C6.1 matches across the extraction's broken "data cen -tre". |
| Numbers found in the article text | 215 | 0 | 216 numeric tokens in claim and support texts. One ("8,760", C20.0) is extracted as "8 ,760". Numbers in the Table 3, Table 4 and Fig. 4 readings, and in all sampled claims, were also checked in context, not just for presence. |
| Reference entries matching the article's reference list | 70 | 0 | 72 citations. The 70 non-null entries match the article's entry at the cited number, including multi-reference ranges (3–5, 23–25, 30–34) and the two different Boyd entries (27 vs 48). The 2 null entries (C20.5.S0, C20.6.S0) are inline URLs in the Methods with no reference-list entry, so null is correct. No entry is invented or completed. |

**Readings of images, reported separately:**

- Extended Data Table 1 (PDF p.13 is an image; only its title extracts). C25.0–C25.4 are
  all `paraphrased` and name the table. All five rows match the rendered image, including
  the completeness cells "as printed" (score 4 reads "<40% … adequate period, or 60–79% …
  shorter period"). One number (59, in C25.1) exists only in the image. It is correct by
  eye.
- Fig. 4: the bar totals are text labels in the PDF and are extracted. The 24 totals in
  C11.6.S0 match both the extraction and the image. Segment readings (use phase largest
  in grid bars, fluid small, server dominant in renewable GHG bars) are correct by eye and
  correctly say segment values aren't printed.
- Fig. 1 and Fig. 2 readings (C4.2/4.4/4.5 S0, C5.6.S1) match the extracted labels and
  captions.
- The Vcore equation (C17.3) and the use-phase equation (C20.0) are typeset text, not
  images. They are paraphrased consistently with the printed equations.

## A5. Detail and readability

- **Size:** 26 steps, 164 claims, 74 support items.
- **Spread:** 17 steps cover the 8 pages of main text, 7 steps cover the 3 pages of
  Methods, and 2 cover back matter and Extended Data. Density follows the article: the
  statistics-heavy introduction (15 claims over steps 1–2) and the engineering-design
  section (21 claims over steps 13–14) get the most. The figures and tables sit with the
  passages that invoke them, as the reading plan says.
- **Thinnest steps:** step 16 (future work, 3 claims) and step 24 (data availability,
  contributions, disclosures). Step 24 is the article's own back matter and records
  provenance a researcher would want. It isn't padding.
- **Can a reader follow the argument from the reading alone?** Yes. The `moves` fields
  name each step's function. The `meaning` fields are short and don't repeat the claims.
  Several do real reading work, all placed in `meaning` rather than claimed for the
  author:
  - the Fig. 1a "polyethylene glycol" vs modelled propylene glycol mismatch (step 8)
  - the abstract's 52% water figure not being a Table 4 saving (steps 9 and 11)
  - more Vcores for cold plate despite fewer added servers than one-phase (step 9)
  - the 10 GW example being illustrative (step 15)
- **Repetition:** the Methods steps restate some main-text material (metrics, lifetimes,
  fluids), but so does the article. The run mostly records only what the Methods add.
- **Structural gap:** several of the article's own quantitative conclusions aren't linked
  to the in-article evidence behind them. C13.0 ("Our LCA has shown …") and C15.0 (the
  "at least 15/15/31%" conclusion) carry no support item pointing to Table 4 or Fig. 4.
  C15.0's only support is ref. 44. C9.4, C9.5 and C10.0 likewise have no link to Table 3
  or Fig. 4. The tables are read in full elsewhere in the reading, so nothing is lost
  for coverage. But the claim→support links, which feed the cross-source comparison,
  are thinner for the conclusions than for the descriptive claims.
- **Citation-only support:** many support items describe a cited work from its title
  ("The authors cite a Nature article on data centre electricity use"). That is all the
  article gives, so it isn't an error, but it carries little evidential content.

---

## Summary for the researcher

This is a faithful, complete close reading. It reads the whole article, including
Methods and the image-only Extended Data table, and catches every item on the claims
reference list. It also records a few claims the list left out, including the
competing-interests statement. Attribution is very clean:

- every sampled claim and support item scored 2
- all 19 verbatim texts are the author's words
- every reference entry matches the article's list, with null used correctly for inline
  URLs
- every number checked, including the full Table 3, Table 4 and Fig. 4 readings, is right

Hedges and scope conditions are kept consistently. The reading's own observations,
some of them sharp (the PEG/PG mismatch, the 52-vs-48 water figure), stay in `meaning`
and aren't attributed to the authors. The weaknesses are small:

- one out-of-sample claim (C1.6) gives SBTi's "must" to the authors
- the headline quantitative conclusions (C13.0, C15.0) aren't linked to Table 4 or Fig. 4
  as support, which matters a little if the comparison relies on claim→support pairs
- many support items are just descriptions of cited works by title

The run's close-reading instructions (`prompts/close-reading.md`) weren't in the folder,
so compliance was judged against the rubric's summary of them.
