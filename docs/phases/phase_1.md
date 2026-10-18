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

**Response:** 




