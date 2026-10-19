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

**Response:** Committed as c96d57e on main with your phase_1.md log. A rerun now keeps the failed run's record as failed_run_<n>.json. All 83 tests pass, Ruff and mypy are clean, the tree is clean and nothing is pushed.

## 12. Start with Barnett 

**Prompt:** I am working on the Barnett article right now. I am writing my notes on a whiteboard and then Chat is transcribing them. I was thinking we could start with that article and compare my notes?

**Response:** Yes, starting with Barnett is a good idea, for two reasons.

- It's a cheap test run. Barnett is the shortest article at 7 pages, so its 6 runs are the cheapest in the experiment. They also exercise the runner and records end to end before you spend money on lei.
- Your notes give the comparison a reference point. Phase 2 needs your own reading of each article to check the judge against. Notes you wrote before seeing any model output are exactly that.

## 13. Prepare Barnett for analysis 

**Prompt:** Prepare Barnett for analysis 

**Response:** Barnett is prepared in outputs/preparation/ in 5.2 seconds, with 1 gap (Table 1) and 1 crop. The text has a reading-order break on page 1: front matter lands mid-sentence. Nothing was edited by hand, and nothing is paid or committed.

**Pending decision:** Leave the page 1 break as extracted, or fix it by hand?

## 14. Fix page 1 break

**Prompt:** Fix page 1 break

**Response:** The opening sentence of Barnett's prepared text is whole again, with the front matter moved above the Introduction heading. Barnett's text arm is ready to run whenever you want to start its 6 runs.

## 15. Run Barnett 

**Prompt:** Run Barnett 

**Response:** All six Barnett runs returned an analysis, each in one attempt, for $1.97 total. The Astra text + crops run failed once on a connection error that cost nothing, and the rerun worked. Every run used the same prompt and schema, and no code had uncommitted changes.

## 16. Compare Barnett runs

**Prompt:** Compare the six Barnett analyses against my notes.

**Response:** All six analyses get the article's basics right, and none of them makes your main critique. That critique stays your own contribution. Below is how they compare with your notes, checked against the article where it mattered.

Where they match your notes
Methods: all six match the methods passage you quoted: a targeted review across three source types, peer-reviewed sources first, no original data. One small slip: Astra on the PDF adds "and other technology providers" to Google, Microsoft and AWS. That isn't in the methods text.
Thesis: all six put the governance argument in the research problem, and roughly half of each one's central claims are about policy. None of them reads the paper as a purely technical survey.
Numbers: I found no number in any analysis that's missing from the article. That's a loose check on digits only. Where I checked context, the numbers were attached to the right things.
Attribution: every central claim in all six is labeled as the author's statement. I spot-checked 7 of the most distinctive ones ("qualitatively different," "market failure," "governance failure," the nuclear and SMR point, curtailment, "irreversibly"), and all 7 are in the article.
Your takeaways
Your takeaway	What the analyses do
1. Moral turn	All six call the benefit-based framework a "normative trade-off" and fault it for having no criteria for judging benefit. None asks why a sustainability question becomes a justification question.
2. Semiconductors	You're right. The article mentions semiconductors four times: the abstract, one definition, a scope exclusion and a research priority. All six record "out of scope," but only as the author's own disclaimer. None notices that the abstract lists it as one of three pathways.
3 & 5. Buried thesis	None of them sees it. They report the policy argument as central, but nothing about proportion: that the thesis arrives at the end, after a long technical setup.
4. The examples show it works	Most of the analyses lean the other way (5 of 6). They say the "choices, not necessity" conclusion assumes the successful examples would work elsewhere, and that the paper never shows this. This is a real disagreement between you and the analyses, and it's worth your judgment.
What they found that your notes don't have
Unreproducible review methods (all six): no search strings, no screening procedure, no count of included sources.
Figures that aren't AI-specific (3 of 6): many of the numbers are about data centers in general, not AI workloads.
A mismatched citation (Sol high on the PDF only): the article cites Jain (2025) for a claim about water transparency. I checked the reference list, and that source is about AI in chip verification. That's a genuine catch.
Your open questions, answered from the article
The consumption table is U.S. data centers. The 2028 figure of 60–124 billion liters covers hyperscale facilities alone, which is what your asterisk was marking. Only Sol high on the PDF kept that qualifier.
Google's 20 billion liters is "annually in recent years." The 2024 in your notes is the year of the report, not of the data.
Hainan (China) and Project Natick (Microsoft) are separate subsea projects, and Microsoft's is the one that was discontinued.
AWS reclaimed water is its own row in Table 1. It isn't part of waterless systems.
By configuration

This is one article and my reading. It's evidence for Phase 2, not a verdict.

Configuration	Cost	Time	What stood out
PDF, Sol medium	$0.16	234 s	Solid, middle of the pack
PDF, Sol high	$0.24	356 s	Most thorough: most evidence, most model-inferred assumptions, the only one that kept the 2028 qualifier, the only Jain catch
PDF, Astra low	$0.64	133 s	Leanest; the one embellishment in its methodology
Text, Sol medium	$0.14	195 s	Similar to PDF Sol medium
Text, Sol high	$0.20	319 s	Rated how well the evidence supports only 9 of its 33 claims; the PDF version rated 27 of 29
Text, Astra low	$0.59	140 s	Plus one free failed attempt

On Barnett, Astra costs 2.5 to 4 times as much as Sol and shows no visible quality advantage. Sol high on the PDF did the most critical reading.

## 17. Modify prompt to examine gaps

**Prompt:** So why didn't the system examine the gap I identified, and do you think the prompt needs to change?

**Response:** They didn't miss it by accident. The prompt never asks for it.

Why the analyses didn't examine your gap

Your critique is about the whole document: where the thesis appears, what most of the length is spent on, and whether the abstract's promises are delivered. The prompt only asks for assessment one claim at a time.

The only assessment the prompt asks for is per claim. support_assessment asks whether the reasons offered for a single claim meet that claim's own wording (prompts.py:85-128). Nothing asks how the paper is built, how much space each part gets, or whether the body delivers what the abstract announces.
The schema has nowhere to put a whole-paper judgment. The analysis has a research problem, claims, methodology, assumptions, limitations, proposed solutions and open questions. Every one of those is a list of separate items. A model could have squeezed a structural critique into limitations, but that field reads as "limitations of the study."
The prompt pushes toward a charitable reading. It says "reconstruct the source's own argument on its own terms" (line 13). It also says not to "invent an objection the passages you found do not themselves raise" (line 120). A critique about proportion isn't tied to any single passage, so a careful model following those lines would hold it back.

So the models did what they were told, and did it well: claim by claim. Your takeaways work at a level the system doesn't have.

Should the prompt change?

I think yes, but with care.

Why yes: the gap goes to what you said you need from this system: a map of the paper before you read it. "The real thesis is the policy argument at the end, and the technical sections mostly serve as setup" is exactly the map that would have saved you hours on Barnett. An analysis that can't say that is missing the level most useful to you.

Why with care:

One article is thin evidence. Your README describes exactly how v1 went wrong: every problem got absorbed into the design. Any change should ask a general question (how is the argument built, does the conclusion follow from the body, does the abstract match what's delivered), not "find buried theses."
It probably needs a schema field, not just prompt text. One whole-document assessment field would keep this critique out of limitations. That changes the output schema, which is held constant in the experiment, so it would need its own ADR.
Timing: only Barnett has run so far. Changing now costs one rerun of its 6 cells, about $2, and the experiment stays consistent: the same prompt and schema across all 18 runs. Changing after katakam and lei means rerunning 18 cells, or splitting the experiment across two prompts.

My recommendation: decide before running katakam and lei. If you agree that a whole-document assessment is something the system must do, make the change now (one schema field plus a short prompt paragraph, recorded in an ADR), then rerun Barnett. If you're unsure, the alternative is to keep the prompt as it is, finish Phase 1, and record this as a Phase 2 finding. That keeps the experiment clean, but it puts the fix off until after the collection's configuration is chosen.

## 18. Add whole-document assessment field

**Prompt:** I want to add a whole-document assessment. Chat suggested this. What do you think?

Assess the reasoning connecting the source’s central findings to its main conclusions and recommendations, even when those connections span multiple claims or sections. Identify the premises needed for those conclusions to follow, including any value judgments. Explain which premises the source supports, which it states without support, and which remain implicit. Distinguish whether a recommendation is justified from whether its implementation is adequately specified. Always assess this central reasoning; keep assessments of secondary claims selective.

**Response:** Chat's text is good on the reasoning chain, but it doesn't reach the gap you identified.

What it covers well

"Including any value judgments" goes straight at your Takeaway 1. It would push a model to say that the benefit-tiering framework rests on an unargued premise about whose needs count more. One analysis came close on its own: Astra on the text arm listed "essential domestic and agricultural water needs should carry greater weight" as an assumption. This makes that the norm.
"Supported, stated without support, or implicit" fits the bridge from "it works" to "we need policy." It would make the model show whether the water-pricing argument actually carries the conclusion.
Separating "justified" from "adequately specified" is a real improvement. All six analyses blurred the two: "the framework lacks criteria" is an implementation complaint, and it says nothing about whether the recommendation is justified.

What it misses: your Takeaways 2, 3 and 5 are about how the document is built, not about logic: where the thesis appears, how much of the length serves it, and whether the body delivers what the abstract promises. Chat's text only asks whether the conclusions follow. A model could answer it perfectly and still never say "the thesis arrives at the end, after a long technical setup," or "the abstract names semiconductors as one of three pathways and the body doesn't analyze them."

I'd add one sentence:

Describe how the document is organized relative to that reasoning: where its main conclusions are actually established, how much of the document develops them, and whether the scope the abstract and introduction promise is what the body delivers.

It's worded to describe rather than criticize, so it shouldn't invite routine fault-finding. The prompt's existing "calibrated judgment, not routine criticism" line still applies.

It also needs somewhere to go. Without a field of its own, a model would scatter this across support_assessment, assumptions and limitations, which is roughly what happens now. I'd add a single required text field to the analysis, something like argument_assessment, holding the whole-document assessment as prose. That changes the output schema, so it needs an ADR.

One overlap to watch: the prompt already says "Most claims will not need this field" about support_assessment. Chat's last sentence, "keep assessments of secondary claims selective," agrees with that, so the two don't conflict. Just place the new paragraph so it's clearly about the new field.

**Pending decision:** If you're happy with Chat's text plus that sentence, the change is:

1. One new field in models.py.
2. A short paragraph in SYSTEM_PROMPT.
3. ADR-0010.
4. Updating the tests that build analyses.
5. Rerunning Barnett's 6 runs, about $2.

Do you want me to go ahead?

## 19. Modify prompt instructions

**Prompt:** Chat proposed this:

Examine how the document’s organization supports its reasoning. Distinguish where its main conclusions are announced, where the supporting arguments are developed, and where the conclusions are restated. Assess whether that development adequately supports the conclusions and whether the body delivers the scope promised by the abstract and introduction. Identify substantive gaps with specific passages; do not treat section placement or length alone as evidence of weakness.

**Response:** This version is better than my sentence in two ways, and it loses one thing you care about.

Better than mine:

"Announced, developed, restated" is sharper than my "where they're established." It matches a distinction the prompt already makes ("a stated intention to argue something later" versus "the argument actually developed," lines 113–115), now applied to the whole document.
"Identify substantive gaps with specific passages" keeps the assessment grounded, so the model can't just give an impression.

The problem is the last clause. "Do not treat section placement or length alone as evidence of weakness" is a fair rule: a thesis that comes at the end isn't a flaw in itself. But Chat also dropped "how much of the document develops them." Together, a model will most likely say nothing about proportion. Proportion is half of your Barnett critique: most of the paper is technical setup, and the policy thesis gets little development. Part of that survives in "whether that development adequately supports the conclusions," but only as a judgment of adequacy, never as a description of the layout.

Fix: have the model describe proportion as a fact, and keep the guard against judging on it alone:

Examine how the document's organization supports its reasoning. Distinguish where its main conclusions are announced, where the supporting arguments are developed, and where the conclusions are restated, and describe how much of the document each part occupies. Assess whether that development adequately supports the conclusions and whether the body delivers the scope promised by the abstract and introduction. Identify substantive gaps with specific passages; do not treat section placement or length alone as evidence of weakness.

The description gives you the map you wanted ("the thesis is developed in the last two sections; the first two-thirds is technical background"). The guard still stops the model from calling that a flaw unless it can point to passages where the development falls short.

This paragraph would follow Chat's first paragraph, with both going into the one new whole-document field. Do you want me to make the change (field, prompt, ADR, tests), then rerun Barnett?

## 20. Implement Changes, Create ADR-0010

**Prompt:** Yes, implement the changes (field, prompt, ADR, tests). Do not rerun Barnett yet.

**Response:** The argument_assessment field, the two prompt paragraphs, ADR-0010, the tests and the docs are in place, and all 84 tests, Ruff and mypy pass. Barnett hasn't been rerun and nothing is committed. Note that outputs/ isn't in .gitignore, even though the README says it stays out of git.

## 21. Rerun Sol 6.1 High PDF with new system prompt

**Prompt:** Rerun Sol 6.1 High PDF to see if it changes with the new system prompt.

**Response:** The change works. The rerun's `argument_assessment` is a 603-word assessment of the whole document, the level the old analyses never reached. On your main critique, though, it engages your point and comes to the opposite conclusion.

**How it lines up with your takeaways**

| Your takeaway | New assessment |
| --- | --- |
| **1. Unexplained moral turn** | It names the value premises (water is a finite common resource, allocation should be equitable, uses differ in necessity), but it calls that bridge "explicit rather than hidden." It finds the implicit premise elsewhere: that institutions can legitimately compare benefits at all. It **partly disagrees** with you. |
| **2. Abstract promises more than the body delivers** | **It catches this in general form:** "the broad title and opening discussion of a global water footprint exceed the operational-blue-water evidence actually synthesized." It doesn't name semiconductors specifically. |
| **3 & 5. Buried thesis; most of the paper is setup** | **It describes the proportions:** technical material on pages 2 to 5, governance on 5 and 6. Then it judges the reverse of you: the technical sections give the governance argument "a substantive technical foundation rather than merely restating the abstract." It also points out that the abstract announces the policy thesis on page 1. **It disagrees with you.** |
| **4. The examples show it works** | The same as before: the examples support only the narrow point that some facilities avoid high water use. Going further needs an "untested portfolio-feasibility premise." |

It also adds something close to your overall impression: the conclusion "is more decisive about political choice and irreversible consequences than the review's own… uncertainties warrant."

**What this means:** the original problem was that the system couldn't see your critique at all. Now it sees the same structure and argues the other side. That's a genuine disagreement about the paper, not a blind spot, and it's exactly what your human-scored sample in Phase 2 is for. Either reading is defensible. Yours says the technical sections are mostly a setup. The model's says they supply real premises: the electricity penalties and scaling limits are why technology alone isn't enough. Deciding which one is right is your call, not mine or the model's.

**Cost:** about the same as before, $0.23 against $0.24. The longer prompt added about 260 input tokens, and output came out slightly shorter.

**Before keeping this run as part of the experiment:** its record shows `code_uncommitted_changes: true` and the old commit, because I ran it before committing. If the prompt change stays, commit first, then rerun all six Barnett cells, so every record carries the same, committed fingerprint.

## 22. Rerun the other 5 Barnett runs with the new system prompt

**Prompt:** Let's rerun the other 5

**Response:** The 5 runs are going in the background, one after another, under the new prompt. That should take about 20 minutes. When they finish, I'll move them into `after_adr_0010/` and compare the six new whole-document assessments.

These runs will also show the prompt change as uncommitted in their records, like the Sol high rerun, because nothing has been committed yet.

All five reruns returned an analysis on the first attempt. All six new runs are now in `after_adr_0010/`, next to the originals in `before_adr_0010/`.

## What the six new assessments say

**All six describe the paper's structure now.** Each says where the thesis is announced (the abstract), how much space the technical sections take (most of pages 2–5), and where governance is developed (pages 5–6). Before the change, none of them did this.

**On your main critique, all six disagree with you.** They say the technical sections give real reasons for the governance argument rather than just setting it up: electricity penalties, low water prices that favor evaporative cooling, allocation rules that hold during drought. Astra on the PDF puts it most directly: the structure makes the bridge "explicit rather than leaving governance as an unrelated conclusion."

**All six agree with you that the conclusion goes further than the body supports.** Each says the closing claims (outcomes are "choices, not necessity," political will is what's missing, water stress is "irreversible") are stronger than the evidence. They also note that Section 4 itself documents real technical and scaling limits.

**On your other takeaways:**
- **Moral turn (1):** all six say the value premise is stated openly, not hidden, and that no method for ranking benefits is given. Sol medium on the text comes closest to your reading: digital water sobriety "adds a normative premise rather than simply following from" the water figures.
- **Abstract versus body (2):** the four Sol runs say the abstract's broad footprint language goes beyond what the body delivers. The two Astra runs say the body "broadly delivers." None names semiconductors.

**New catches:**
- **Meta's Luleå data center.** Both Sol runs on the text arm used Table 1's footnote: the annual withdrawal figure can't show how efficient a hyperscale site is, because the facility's IT capacity isn't disclosed. That bears directly on your Takeaway 4, which uses Meta Sweden as a success. The footnote only shows up in the prepared text, which may be why the text arm caught it.
- **Heat recovery.** Four of the six say the conclusion promises firmer water benefits than Section 4.5 supports.

## Why all six might agree

When all six land on the same verdict against you, it could mean the paper reads that way. It could also be the prompt. "Reconstruct the argument on its own terms" and "do not treat section placement or length alone as evidence of weakness" both push the models toward the charitable reading. The guard against judging on length was meant to stop routine fault-finding. It may also be stopping a critique like yours. One article can't tell these two apart. Katakam and lei, with your notes on them, will show more.

## Cost and size

| Configuration | Before | After | Assessment |
| --- | --- | --- | --- |
| PDF, Sol medium | $0.16 | $0.17 | 601 words |
| PDF, Sol high | $0.24 | $0.23 | 603 words |
| PDF, Astra low | $0.64 | $0.55 | 360 words |
| Text, Sol medium | $0.14 | $0.14 | 572 words |
| Text, Sol high | $0.20 | $0.19 | 488 words |
| Text, Astra low | $0.59 | $0.50 | 357 words |
| **Total** | **$1.97** | **$1.77** | |

The new runs cost less overall but produced fewer claims. Astra went from 21 to 16 claims on the PDF and from 24 to 17 on the text, and Sol high on the text from 33 to 25. The new field may be taking space from the claim list. It's worth checking whether any claims you care about went missing.

One more thing: all six new records show `code_uncommitted_changes: true` and the old commit, because the prompt change still isn't committed.

## 23. Claims lost

**Prompt:** But here's the problem. After ADR 0010, we lost substantial claims. We could split up the whole document analysis from the claims, but that would require two paid runs... I asked Chat if we could give the agent two tasks, and it said yes. 

Yes. One agent, one call, two explicit tasks:

Analyze the individual claims: capture the distinct substantive claims, their evidence, important qualifications, and assessments of their support.
Assess the whole document: use that reconstruction to examine how the conclusions follow, how the argument is organized, and whether the body delivers its promised scope.
Tell it explicitly that task 2 supplements task 1: it must not replace distinct claims or their assessments with a broad discussion in argument_assessment.

**Response:** Yes, I think that could help.

**Why it should help**
- It names the cause directly. Two tasks, with "task 2 supplements task 1, it must not replace distinct claims," goes straight at what happened: the assessment field swallowed the claim work.
- The order matches the schema. Claims first, then the assessment built on them. argument_assessment is already the last field, so the model writes it after the claims anyway.
It's still one call. Same cost, no new architecture, no second-call failure case to design.

**Two adjustments I'd make to the wording**
- "Assessments of their support" should keep its current limit. The prompt already says most claims won't need a support_assessment. If task 1 reads as "assess every claim," the outputs get much longer and more expensive. Something like "and assessments of their support where the claim's importance and wording call for it."
- Remove the sentence that probably caused this. "Keep assessments of secondary claims selective" should either go or say plainly that it's about support_assessment, not about which claims to extract. Otherwise the new framing and the old ambiguity sit side by side.

What it can't guarantee: a wording fix can only nudge the model. And we still don't know how much the claim count varies between two runs of the same prompt. So test it on one or two runs before rerunning all six. Good candidates are the two with the biggest drops: Sol high on the text (33 → 25) and Astra on the PDF (21 → 16). That's about $0.70 for both, and if their claim lists come back to roughly the before level with the technology claims separate again, it worked.

Bookkeeping: ADR-0010 quotes the prompt text word for word, so changing it means either a short ADR-0011 or a note in the ADR saying the wording was revised. And if it works, Barnett's six runs get redone a third time, into another folder next to the two existing ones.

## 24. One call, two tasks

**Prompt:** I said to tell it to run two tasks. I thought we are building agentic AI, which can run multiple tasks before closing the instance.

**Response:** Yes, we can do that, and it's a more natural fit than I made it sound. First, what the system actually does today, because it explains the confusion.

Right now, an "agent" here is a single request. We send the article and the instructions, and the model returns one JSON analysis. The README calls the three parts "agents," but none of them runs in steps on its own. There's no instance that does task 1, then task 2, then closes.

What you're describing is one conversation with two turns:

Turn 1: "Analyze the individual claims." The model returns the claims, evidence and per-claim assessments, using exactly the instructions we had before ADR-0010.
Turn 2, in the same conversation: "Now assess the whole document, building on your claim analysis." The model sees the article and its own turn-1 output, and returns only the argument_assessment.

The code already does something like this. When the model's first answer doesn't fit the schema, the correction attempt goes back into the same conversation with the previous answer and a follow-up message. Task 2 would use the same mechanism, just with a planned second turn instead of a fix-up.

Why it might work better than one call with two tasks

The claims come out exactly as they did before ADR-0010. Turn 1 has the old instructions, and nothing about the assessment can crowd out the claims.
Turn 2 builds on finished claims. It assesses the argument with the full reconstruction in front of it instead of writing both at once.

What it costs

Money: less than double. The second turn re-sends the article, but the API can cache a repeated prefix and charge it at the cached rate, which is $0.10 instead of $2.00 per million tokens for Sol, and $1 instead of $10 for Astra. Whether caching actually kicks in, we'd see in the run records, which already log cached_input_tokens. Most of the extra cost is turn 2's output, roughly the length of one assessment plus its reasoning.
Code:
analyze_source makes two requests instead of one.
The schema splits in two: claims without the assessment, and the assessment on its own.
Each turn gets its own attempt record and its own correction attempt.
There's one new failure case to settle: turn 1 succeeds and turn 2 fails. Do you keep the claims and report the assessment as missing? (ADR-0005 suggests yes: a missing assessment is reported, not a reason to withhold the claims.)
That's an architecture change, so it needs its own ADR.

The two options side by side

	One call, two tasks (Chat's wording)	One conversation, two turns
Do claims return to the before level?	Probably; it's a nudge	Yes; turn 1 is unchanged
Cost per run	Same as now	More, though caching should keep it well below double
Code change	Prompt wording only	analysis.py, schema split, records, ADR
New failure case	None	Turn 2 can fail after turn 1 succeeds

Both can be tested on one or two runs before rerunning Barnett. Which one you build is your call. The two-turn version is the closer match to what you described.

## 25. ADR 0011: Two-Task Framing

**Prompt:** Propose this in ADR 0011:

One way to avoid choosing blind: try one call first, since it's only a prompt edit plus about $0.70 to test on the two runs that lost the most claims. If the claims come back, you're done. If they don't, you build two turns knowing you need them.

**Response:** ADR-0011 is written as Proposed. It contains the draft two-task prompt wording, the $0.70 test on two Barnett runs, what counts as the claims coming back, and two turns as the fallback. It's listed in the ADR index, REPOSITORY.md and the README tree. The prompt is unchanged and nothing is committed.




