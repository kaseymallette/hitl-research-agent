# Phase 1 — A/B Testing

Four articles through four configurations — full PDF or extracted text plus
crops, Sol medium or Astra low — producing 16 analyses with usage, cost,
runtime, and preparation effort recorded.

See [Phase 1 in the build plan](../BUILD_PLAN.md#phase-1--ab-testing) for what
this phase builds and what marks it done. Conventions for these entries are in
the [prompt log index](../prompt_log.md).

Entries are numbered locally within this phase, in the order the prompts were
given.

---

## 1. Read the project documentation

**Prompt:** Hi Claude! We are starting phase 1. Please read the @README.md, @docs/DESIGN.md, @CLAUDE.md and @docs/BUILD_PLAN.md to understand the project and the goals of phase 1.

**Response:** What Phase 1 does: it builds the evidence for Phase 2 and doesn't pick a winner. The matrix is 4 articles × 2 input workflows (pdf vs. prepared text + crops) × 2 model configs (gpt-6.1-sol at medium, gpt-6-astra at low), for 16 analyses in outputs/ab_testing/<slug>/<config>/.

The three tasks, in order:

Prepare the four A/B articles with prepare_sources.py. For each one, record the time it took, the gaps (figures, equations, multi-level table headers), the crops kept, and any manual work. That preparation effort counts against the text arm only.
Run the 16 cells with run_analysis.py. Each cell writes analysis.json (exactly what the model returned) and run_record.json (usage, calculated cost, runtime, per-attempt records). The runner asks for confirmation before each run and reports the actual cost as it goes. The projected total is about $10–15, mostly from the Astra cells.
Write summary.csv. It has one row per cell, and it's the only new code this phase needs.

**Pending decision:** Before planning task 1, I'd check two things: whether prepare_sources.py already writes a prep_record.json with timing and gap counts, and whether run_analysis.py already handles the "failed cell still writes a run record" behavior and the per-run cost confirmation. If it doesn't, either one means a code change, and I'd raise it with you before making it.

## 2. Sol 6.1 Medium vs. Sol 6.1 High

**Prompt:** But what if we should be looking at 6 Astra low vs. 6.1 Sol Medium and 6.1 Sol high?

**Response:** The case for adding Sol high

The current design changes two things at once. Astra low and Sol medium differ in both the model and the reasoning effort. If Astra comes out ahead, you can't tell whether the model made the difference or Sol simply wasn't given enough effort.

Adding Sol high separates those two effects within Sol. It also tests the cheaper alternative that matters most for Phase 2: whether Sol with more reasoning matches Astra at lower cost than Astra. Reasoning tokens are billed as output tokens, so Sol high costs more than Sol medium, but it starts from a rate one-fifth of Astra's. How many extra tokens it uses is unmeasured, so I can't tell you its cost from the records we have.

What it costs

API spend. You'd go from 16 to 24 analyses. The extra 8 are Sol cells, so the spend rises less than the count does. The ~$10–15 projection was already based on a single article.
Phase 2 cost. The judge runs on 24 analyses instead of 16, across several metrics each.
Your review time. This is probably the binding constraint. ADR-0008 kept the experiment to four articles partly because "Four is what the budget and the human scoring effort support." Going from 16 to 24 analyses grows the human-scored sample by half again, or spreads it thinner.

**Pending decision:** My own reading is that the confound is real and Sol high is the cheapest way to resolve it. Whether the extra review time is worth it is for you to decide.

## 3. 3 x 2 x 3 proposal

**Prompt:** What if we did a 3 x 2 x 3 design instead? 3 articles, 2 input workflows (pdf vs. prepared text + crops), and 3 model configs (gpt-6.1-sol at medium, gpt-6-astra at low, gpt-6.1-sol at high)?

**Response:** Three articles gives 3 × 2 × 3 = 18 analyses, about the same as the original 16, and keeps Sol high. The design stays balanced and the confound gets resolved. The cost is coverage, and how much that matters depends on which article you drop.

What you lose

Each cell rests on three articles instead of four. Four was already "an initial comparison, not a conclusion" in ADR-0008. With three, one unusual article moves the result more.
Possibly the input contrast. The text-vs-PDF comparison only shows up on articles with figures, equations and complex tables, because those are what preparation struggles with and what produce crops. If you drop the article where preparation struggles most, the experiment says less about the thing ADR-0008 was written to settle.

Which article to drop

Article	Pages	Role
lei	60	stress case for PDF-arm cost; the build plan calls this out
barnett	7	cheap case
kanban	18	middle
katakam	20	middle

Keeping lei and barnett preserves the page-count spread the build plan says was deliberate. That leaves kanban or katakam. The two are close in length and both cover desalination, so on paper either can go. I don't think the choice between them should be made on page count alone, though.

**Pending decision:** Decide which article to drop and proceed with the 3 x 2 x 3 design.

## 4. Drop katakam

**Prompt:** Let's get rid of kanbur because we have two articles about water desalination and katakam is the 2027 article

**Response:** Agreed, and the page-count spread survives: barnett at 7 pages, katakam at 20 and lei at 60. (Earlier I wrote "kanban"; I meant kanbur.)

Assuming Sol high is in, the matrix is now 3 articles × 2 input methods × 3 configurations = 18 analyses:

	Sol medium	Sol high	Astra low
Full PDF	3	3	3
Text + crops	3	3	3

I checked the references. No code depends on which articles sit in ab_testing/, since run_analysis.py takes a --pdf path. kanbur is mentioned only in BUILD_PLAN.md and sources.yaml.

What I'd change (I haven't edited anything yet):

A new ADR-0009 recording the revised matrix and why: adding Sol high separates model from effort, and the experiment is cut to three articles to keep review time roughly where it was. It marks ADR-0008 as superseded on those points, since ADR-0008's notes say it gets superseded rather than edited. ADR-0008's other decisions still stand: measure before choosing, prepare_sources.py stays frozen, and an article with no crops still counts. ADR-0009 would restate or point to them so they don't lapse.

BUILD_PLAN.md Phase 1: update the article table, the configuration table and slugs (adding *__gpt-6.1-sol-high), the cost paragraph and the acceptance criteria (18 files, three articles).
README.md: update the A/B section and its table, the GPT-6.1 Sol vs. GPT-6 Astra paragraph, the "four of which" line and the Phase 1 roadmap row.

**Pending decision:** One decision needed before I start: should kanbur's PDF move from data/research/ab_testing/ to data/research/ so the folder matches the experiment? That changes its pdf: path in sources.yaml but nothing else. Leaving it in place is simpler, but then the folder name no longer describes what's in it.

## 5. ADR-0009

**Prompt:** Let's create ADR-0009 to record the revised matrix and why we made the changes. I moved kanbur's PDF to data/research/ so the folder matches the experiment.

**Response:** Created ADR-0009 documenting the 2 × 3 matrix with Sol high effort added and kanbur dropped, keeping the run count at 18 rather than 24. The ADR explains the rationale and amends ADR-0008's matrix while preserving its other decisions.

**Pending decision:** Check prepare_sources.py and run_analysis.py against Phase 1 next?

## 6. Check prepare_sources.py and run_analysis.py against Phase 1

**Prompt:** Yes, check prepare_sources.py and run_analysis.py against the Phase 1 requirements before we prepare the three articles.

**Response:** Short version: prepare_sources.py is fine to run on the three articles now. run_analysis.py has two problems that would break the experiment's "prompt held constant" requirement, plus a few record-keeping gaps. All of them should be fixed before the first paid run.

prepare_sources.py: ready to run

It writes prep_record.json with everything the build plan asks for, except one item:

Timing: recorded as wall-clock seconds for extraction and writing.
Gaps: each annotation carries its kind (figure, table, equation) and page. Multi-level table headers are marked separately from plain tables.
Crops kept: listed under retained_images.
Manual intervention: not recorded. The script has no field for it, and since the script is frozen (ADR-0008), it can't gain one. Your own time (reading the prepared text, rendering pages to check a figure) has to go somewhere else, such as a short preparation note per article.

One known limit, already documented in the script: a figure with no caption gets no annotation and no crop. That makes the crop count a lower bound on what preparation actually missed.

run_analysis.py: what to fix before running

These two make the prompt differ between the arms. The prompt sends the model Source title: and Source type: lines (prompts.py:193). The text arm takes both from sources.yaml. The PDF arm takes the title from the PDF's own metadata and the type from --source-type, which defaults to peer_reviewed_paper (run_analysis.py:66-82).

barnett is source_type: other in sources.yaml, so its PDF cells would see a different type than its text cells.
lei has no title in its PDF metadata, so the PDF arm refuses to run unless you type the title by hand. A typed title must match sources.yaml exactly, or that cell's prompt differs too.

**Pending decision:** The fix is for the PDF arm to read title, type and the rest of the provenance from sources.yaml, the same way the text arm reads its provenance.json. That also gives the PDF arm's analysis.json complete provenance (authors, DOI). Phase 3 needs that to reuse those analyses.

## 7. Fix run_analysis.py

**Prompt:** Let's fix run_analysis.py to read title, type and the rest of the provenance from sources.yaml, the same way the text arm reads its provenance.json. That also gives the PDF arm's analysis.json complete provenance (authors, DOI). Phase 3 needs that to reuse those analyses.

**Response:** I've made both arms of run_analysis.py take their provenance from sources.yaml. A barnett PDF cell and its text cell now send the same Source title: and Source type: lines in the prompt, and lei no longer needs a hand-typed title. All 76 tests pass, including 3 new ones, and Ruff, formatting and mypy are clean. Nothing is committed.

What changed in run_analysis.py

One function builds provenance for both arms. The PDF arm passes it the manifest entry for its slug. The text arm passes it the provenance.json that preparation copied from that same entry. Because both go through the same code, one arm can't quietly diverge from the other.

The PDF arm stops if its slug isn't in the manifest. It no longer falls back to the PDF's embedded metadata or to the current time for retrieved_at. I loaded the real entries for barnett, katakam and lei through it, and each comes back with its title, authors, type and DOI.

A new --manifest flag, defaulting to data/research/sources.yaml.

One interface change to flag: I removed --title and --source-type. They were the way the two arms could end up with different prompts. --source-type would also have done nothing now, because every manifest entry has to have a type. If you'd rather keep --title as a deliberate override, it's easy to put back.

Tests (test_run_analysis.py):

the PDF arm gets the manifest's title, authors, type, DOI, date and retrieved_at
both arms produce identical provenance for the same article
a slug with no manifest entry is refused

I also updated the runner's entry in REPOSITORY.md. I didn't touch your phase_1.md edits.

**Pending decision:** Still open: each run generates a new random source_id, so the 6 cells for one article each get a different id. The model's own docs ask for the id to be reused whenever a source is reanalyzed. Nothing reads it in Phase 1, but Phase 3's reuse of these analyses will need a fixed id per source. Items 3–6 from the review (cost of failed cells, prompt and schema fingerprints, a reasoning-token total, half-written directories) aren't done yet.


## 8. Two separate IDs

**Prompt:** But isn't it like two separate id's? One for each run and one for each article? No?

**Response:** Yes, that's the design, and it's the right one. There are two ids:

id, one per analysis. Each run gets its own, which is correct, because each run is a separate analysis.
source_id, one per article. It should be the same every time that article is analyzed.

The problem is that the second id doesn't behave as intended. Nothing ever sets it, so each run makes up a new random value, just as it does for id. barnett's 6 runs end up with 6 different source_ids when they should all share one.

The fix is to give each article a fixed source_id that every run reuses. The simplest way is to compute it from the article's slug, so barnett always gets the same id without anything new being stored.

## 9. Fix source_id

**Prompt:** Let's fix it now. Give each article a fixed source_id that every run reuses. The simplest way is to compute it from the article's slug, so barnett always gets the same id without anything new being stored.

**Response:** I committed the provenance and source_id changes as a6308ab on main. The pre-commit checks passed (Ruff, formatting, mypy), and nothing is pushed.

**Pending decision:** Four gaps from the review are still open in run_analysis.py:

- a failed cell records less cost than was actually spent;
- the run records don't prove the prompt and schema were the same in every cell;
- there's no reasoning-token total per cell;
- a crash can leave a half-written directory.

## 10. Address remaining gaps

**Prompt:** Fix them, retries off

**Response:** The four record gaps are fixed and client retries are off. All 82 tests pass (5 new) and Ruff and mypy are clean. Nothing is committed yet. One gap remains: a rerun after a failure overwrites the failed run's record, so the cost of that failed run is lost.

## 11. Keep failed runs

**Prompt:** Keep failed runs

**Response:** I committed the fix as 3b1b586 on main. The pre-commit checks passed (Ruff, formatting, mypy), and nothing is pushed. A rerun after a failure now keeps the failed run's record as failed_run_<n>.json, since its tokens were billed.

