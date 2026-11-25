# hitl-research-agent

A human-in-the-loop AI research framework for analyzing sources, evaluating arguments, and synthesizing findings across a research collection. The project investigates how AI can support rigorous research while keeping human judgment and intellectual direction central.

> Can AI meaningfully support rigorous, evidence-grounded research?

The experiment that tests it:

> Does structured source analysis improve downstream research quality compared
> with retrieving original source passages directly?

## Purpose

Researchers are right to be skeptical of AI for synthesis: models misattribute claims, drop qualifications, and cite evidence that doesn't support them. This project builds a synthesis process that can be checked at every step, and measures it against a subject expert's judgment. It compares two ways of retrieving from a collection, searching the articles' text (traditional RAG) or searching structured analyses of each article (structured RAG), and then grades the syntheses written from each: whether they found the right material, and whether they represent it faithfully. The [pilot](#the-pilot-literacy) uses a literacy education professor's articles, with her as the judge; the science of reading and water studies apply the process to collections too large to read closely by hand.

## Overview

I’m building this framework to become a better researcher: to work through more literature, make connections across sources, and pursue questions I might otherwise miss. I want AI to help me evaluate the authors’ arguments: whether their evidence supports their claims, whether their methods justify their conclusions, and what assumptions or limitations affect those conclusions.

### Judging the judge

But before I can rely on AI to judge an argument, I need to judge AI. When using models to summarize and analyze articles, I’ve noticed that they can misattribute claims, leave out important qualifications, or attach evidence that does not support their interpretations. This project therefore evaluates both how faithfully the model represents a source and how well it reasons about the authors’ claims. I need to know whether its assessment helps me understand the argument or gives me errors to correct.

### AI as a research assistant?

The justification to use AI to support research still needs to be made, and that is what this system is for.

> Why use AI when I can read the articles and evaluate the authors' arguments myself?

The AI agents need to add something worthwhile, whether that is helping me compare explanations, noticing conflicting evidence, or identifying an assumption worth investigating. *Does this system help me conduct better research that justifies the time and money spent to build and implement it?* *Will I use it to support my research consistently?*

### Traditional RAG

A common approach to answering questions from a collection of documents is retrieval-augmented generation (RAG). The text is extracted from each document and split into chunks. Each chunk is converted into an embedding, a vector that represents its meaning, and the vectors are indexed. A question is embedded the same way, the chunks whose vectors are closest to it are retrieved, and a model answers from them.

RAG treats relevance as similarity: a chunk is retrieved because its wording resembles the question. But a chunk is cut from its place in the argument. It no longer carries which claim it supports, which qualifications the author attached, or whether the claim is the author's own or one the author is citing. Nothing in the index says whether the evidence actually supports the conclusion it sits next to.

### Structured RAG: reading before retrieving

This project's analysis is modeled on how a researcher reads an article instead. A language model takes in a whole text at once, attending across all of it in parallel. The close reading makes it go sequentially, following the argument step by step and recording at each step what the author claims, the support given, and how the step builds on what came before. The claims reference lists what the article itself claims. The argument evaluation then lets the model take a position: whether the evidence supports the conclusions, what the argument assumes, and where it falls short, kept separate from what the author says.

Structured RAG is still RAG. The analyses are split, embedded, and retrieved the same way as the article text; only what is searched differs.

### Is the reading worth it?

The question is whether that reading is worth doing. Does structured source analysis improve downstream research compared with retrieving passages directly from the original documents? Retrieving from analyses means retrieving claims with their support, their qualifications, and a judgment of the argument, rather than passages that sound like the question.

The goal is not to assume that additional analysis produces better research. It is to determine whether that analysis provides measurable value, and under what conditions.

## The pilot: literacy

The pilot measures retrieval with precision and recall on a small set of literacy articles from a professor of literacy education, a subject expert who can judge what is relevant. It comes first because the water articles have no such expert, so nobody can confirm what a correct retrieval is there.

*Planned; waiting on the articles (about three).*

**The experiment, done two ways.** The same comparison as the water study, traditional RAG against structured RAG, measured two ways:

| | Traditional RAG (article text) | Structured RAG (close reading, claims reference, argument evaluation) |
| --- | --- | --- |
| **Phase 1: the expert judges** | precision, recall, nDCG; synthesis graded | precision, recall, nDCG; synthesis graded |
| **Phase 2: generated questions** | recall@5, recall@10, MRR | recall@5, recall@10, MRR |

Both phases start the same way: each article gets the single-source analysis (close reading, claims reference, argument evaluation) through the harness, and both indexes are built from the articles, as in the water study.

**Phase 1: the expert judges retrieval and synthesis (first).**

1. **The expert writes the questions:** 15 in all, 5 of each kind.
   - **Explicit:** the answer is stated in one place in an article.
   - **Conceptual:** the answer needs an idea explained, which may be spread across an article.
   - **Synthesis:** the answer needs more than one article, or more than one part of one.
2. **Retrieve for each question** with both approaches.
3. **The expert grades every retrieved piece:** 0 (not relevant), 1 (partly relevant), or 2 (relevant). She doesn't see which approach retrieved it.
4. **Measure:**
   - **Precision:** the share of retrieved pieces graded 1 or 2.
   - **Recall:** of all the relevant pieces either approach found, the share each one found. Every relevant piece in the pool counts, so this is recall against what the two approaches found together, not against every relevant piece in the articles.
   - **nDCG:** whether the most relevant pieces come back first, using the 0, 1, 2 grades.
5. **Write a synthesis for each question** from each approach's retrieved pieces, with the same model and prompt, citing the pieces it uses.
6. **The expert grades each synthesis** the way the water study's codebook does, without knowing which approach it came from:
   - **Attribution:** does it represent the articles faithfully, credit each claim to the article that makes it, and cite only pieces that say what it claims?
   - **Argument:** are its conclusions supported, qualified, and bounded, and does it say where the articles are silent or disagree?
7. **Compare** the two approaches, overall and by kind of question, on both retrieval and synthesis.

**Phase 2: generated questions (after Phase 1's results).**

1. **A model writes one question for every piece**, a question that piece answers. Pieces come from four sources: the article text, the close reading, the claims reference, and the argument evaluation. Each question's correct answer is the piece it was written from.
2. **Search with each question** and check where its piece comes back:
   - **Recall@5 and recall@10:** how often the piece is in the top 5 or top 10 results.
   - **MRR (mean reciprocal rank):** how high it ranks on average, from 1 (always first) to 0 (never found).
3. **Check against Phase 1:** whether the generated questions rank the approaches the way the expert's judgments do. If they do, generated questions can stand in where there is no expert, as in the water study.

The water experiment continues after the pilot.

## Two studies

| Study | Question | Status |
| --- | --- | --- |
| [**Science of reading**](studies/science_of_reading/) | How is the science of reading defined, simplified, and contested as it moves from scholarship, through the popular press, into state legislation? | Legislation trial run done (six laws); scholarly and popular press next |
| [**Water**](studies/water/) | Why does AI infrastructure use freshwater, and when could other cooling methods or water supplies, including desalination, reduce pressure on local freshwater? | Ten articles analyzed and accepted |

The science of reading study is a collaboration with a professor of literacy education.
The water study came first and is where the harness was built.

Both studies do the same core work: take the claims out of individual
documents, then compare them across documents. Water compares what sources
claim about one question. Science of reading traces how claims change as they travel
between corpora. The experiment runs on the water study first, because all
ten of its articles are analyzed and accepted.

What we're doing, why, and what's been decided is in
[`docs/PROJECT.md`](docs/PROJECT.md).

## Water study: methods

The water experiment uses all ten of the [water study](studies/water/)'s articles, which are analyzed and accepted. Whether and how it applies to the science of reading study will be decided after. It compares two approaches to answering the same research questions from the same ten articles: traditional RAG, which retrieves passages of the articles themselves, and structured RAG, which retrieves from analyses of them. In the code they are `rag` and `structured`.

### Traditional RAG

The baseline is retrieval-augmented generation as it is usually done:

- **Extract** the text of each article from its PDF with [`scripts/prepare_sources.py`](scripts/prepare_sources.py).
- **Chunk** the text into passages of at most 200 tokens, overlapping by up to 25, broken at paragraphs where possible. Each passage is labeled with its article and PDF pages. The ten articles give 1,218 passages, averaging 164 tokens: about the size of an analysis item (177), so the same retrieved-text budget holds about as many pieces for either approach.
- **Embed** each passage with an embedding model (`BAAI/bge-small-en-v1.5`, run locally), which turns it into a vector that places passages with similar meaning near each other.
- **Retrieve** the passages nearest a question, embedded the same way.

### Structured RAG

Structured RAG retrieves from analyses of the articles instead of their text. The framework uses AI to assist with three research activities:

1. **Single-source analysis:** Each source produces three documents:
   - **Close reading:** reconstructs the author's argument step by step, identifying claims, supporting evidence, methods, assumptions, and limitations, without judging it.
   - **Claims reference:** lists the source's own claims, written from the source alone, so the close reading can be checked against it.
   - **Argument evaluation:** the model's own judgment of the argument: whether the evidence supports the claims and the conclusions follow.
2. **Evidence evaluation:** Separate judgments assess whether the close reading accurately represents the source and whether the argument evaluation is justified.
3. **Cross-source synthesis (planned):** Compare findings across a collection to identify agreements, disagreements, gaps, and unanswered questions.

The framework distinguishes what an author states from what the model infers or evaluates. Human review determines which analyses enter the research collection.

![Single source analysis: the close reading and the claims reference feed the close reading judgment; the argument evaluation feeds the argument judgment; both judgments go to review, to accept, revise, rerun, or reject.](studies/water/assets/single-source-flow.svg)

For retrieval, each accepted analysis is split into items: a step of the close reading, an entry of the claims reference, a paragraph of the argument evaluation. Each item is labeled with its article and its kind, so the model's reading and judgment are never presented as what an article says. They are embedded with the same model as the passages. The ten articles give 1,751 items.

### Answering

Both approaches answer the same way. For a question, the nearest items are taken in rank order up to a budget of 4,000 tokens of text. One Codex session on GPT-6.1 Sol at medium effort writes the answer from them with the same [prompt](studies/water/prompts/06_answer.md), citing the items each claim rests on. The budget, model, and prompt are identical for both approaches; only what is retrieved differs. Each answer's record keeps what was retrieved, what was cited, and the tokens used.

A third approach, retrieving from both, was dropped after the trial run because it added a variable without isolating one.

## Water study: results

### The trial

Questions 1, 5, and 8 were answered with both approaches. Both had the same 4,000-token budget and pieces of about the same size, so each got 20 to 30 pieces of text. Each bar on the left is all ten articles: the colored part is the articles retrieved, and its solid part the articles the answer cited.

- **Retrieved:** about the same breadth. Traditional RAG retrieved 7 or 8 of the ten articles, structured RAG 8 to 10.
- **Cited:** traditional RAG's answer cited more articles on question 1 (7 against 5); structured RAG's cited more on questions 5 and 8 (9 against 6 on each).
- **No answer cited an item it was not given.**

An answer leaving some of what it was given uncited is expected: retrieval picks pieces by similar wording, and some are off the question.

![Trial results by question. Articles retrieved of the 10, and cited: question 1, traditional RAG 8 retrieved and 7 cited, structured RAG 8 and 5; question 5, 7 and 6 against 9 and 9; question 8, 8 and 6 against 10 and 9. Items cited of retrieved: question 1, 12 of 23 and 12 of 20; question 5, 17 of 25 and 19 of 21; question 8, 19 of 24 and 22 of 30.](studies/water/assets/trial-retrieval.svg)

<details>
<summary>The numbers as a table</summary>

| Question | Approach | Articles retrieved, of 10 | Articles cited | Items cited of retrieved |
| --- | --- | --- | --- | --- |
| 1 | Traditional RAG | 8 | 7 | 12 of 23 (52%) |
| 1 | Structured RAG | 8 | 5 | 12 of 20 (60%) |
| 5 | Traditional RAG | 7 | 6 | 17 of 25 (68%) |
| 5 | Structured RAG | 9 | 9 | 19 of 21 (90%) |
| 8 | Traditional RAG | 8 | 6 | 19 of 24 (79%) |
| 8 | Structured RAG | 10 | 9 | 22 of 30 (73%) |

</details>

The first trial cut the articles into passages twice the size of the analysis items, so traditional RAG got half as many pieces and reached only 4 to 6 articles. That compared piece sizes, not approaches; the passages were re-cut to match and traditional RAG's answers rerun.

These counts show how much of the collection each answer drew on, not whether it represented the sources faithfully. The answers are in [`studies/water/outputs/answers/`](studies/water/outputs/answers/).

### Full results

All ten questions with both approaches: 20 answers. Not yet run.

### From analysis to codebook

Evaluating the analyses became circular. The close reading needed something to be checked against, so the claims reference was added: a second, model-written list of the article's claims. A judge, also a model, then scored the close reading against the rubric partly by whether it matched that list. Every layer was model-generated and checked by another model, and each one added complexity without adding an independent standard.

The codebook keeps what that design got right and drops the circle. The analysis split reading a source into two epistemic tasks, attribution and argument evaluation. Those two tasks, plus the water question's own distinctions, become the codebook's three dimensions:

- **Attribution:** what do the sources say? Codes come from the rubric's close reading criteria: whether a claim is the author's, whether its qualifications and certainty survive, and whether conflicts and differences between sources are noted.
- **Argument:** does the answer's own argument hold up? Codes come from the rubric's argument evaluation criteria: whether the evidence is weighed, whether the grounds are sufficient, whether warrants and qualifiers are stated, and whether the model's view is kept separate from the author's.
- **Water distinctions:** does the answer keep apart what the water literature keeps apart? Codes come from what the analyses kept running into across the ten articles: withdrawal and consumption, onsite and grid water, water quality, accounting boundaries and units, local pressure, modeled and measured results, and desalination as one option among others.

The codebook's examples are taken from the accepted analyses. Every attribution code is checked against the original article, not against another model's output. Each approach's answers are coded with it, and the approaches are compared code by code. The codes are in the [water codebook](studies/water/CODEBOOK.md).

## The science of reading study

The [science of reading study](studies/science_of_reading/) is a collaboration with a professor of literacy education. It examines how the science of reading is defined, simplified, and contested as it moves from scholarship, through the popular press, into state legislation, using critical discourse analysis across the three corpora. The legislation trial run is done (six laws); the scholarly and popular press corpora are next. Its documents run through [`scripts/workspace.py`](scripts/workspace.py), and whether the experiment applies to it will be decided after the water results.

## The harness

[`scripts/run_single_source.py`](scripts/run_single_source.py) runs the
single-source analysis for one article:

```bash
uv run python scripts/run_single_source.py <slug>
```

**Why Codex.** The setup was chosen by two A/B experiments, judged as blind
head-to-head tournaments ([details](studies/water/README.md#the-ab-experiments)):

- **Barnett** compared models and inputs. GPT-6.1 Sol at medium effort, reading
  the PDF, won. High effort was no better, a costlier model was about four
  times the price without reading better, and the PDF beat extracted text,
  which had needed manual fixes.
- **Kanbur** compared three ways of running Sol: the API, the ChatGPT app, and
  Codex. Codex won every round, narrowly, and medium beat high in the final.
  The API cost $0.55–0.64 a run, while Codex runs within the ChatGPT plan.

Codex also makes each call a scriptable, isolated session, which is what the
harness needs.

- **Five calls, five files.** Each call (the close reading, the claims
  reference, the close reading judgment, the argument evaluation, and the
  argument judgment) is its own Codex session on GPT-6.1 Sol at medium effort,
  reading the PDF. Each writes one file to the article's folder. It runs
  within the ChatGPT plan, with no API key.
- **Independent sessions.** Each session runs in a temporary folder holding
  only the files that call needs, so the reading never sees its judgment and
  no judge sees another's verdict.
- **The prompts are the requests.** Each call sends its prompt file in
  [`studies/water/prompts/`](studies/water/prompts/) exactly as written, so
  any call can also be run by hand by pasting the same file into a new Codex
  session. The science of reading study's prompts are in
  [`studies/science_of_reading/prompts/`](studies/science_of_reading/prompts/).
- **Resumable.** With no option, only the calls whose file is missing run, so
  a stopped run picks up where it left off. `--only 03` reruns one call.
- **Revise in place.** `--revise 01` revises the close reading from its
  judgment, and `--revise 04` the argument evaluation from its judgment; then
  `--only 03` or `--only 05` judges the revision.
- **Only a technical failure stops a run:** Codex exiting with an error or
  timing out, a call's file not written, or a close reading that isn't valid
  JSON. A weak reading is written and judged, never withheld. Codex's event
  log for each call is kept in `.codex_runs/<slug>/`.

[`scripts/build_index.py`](scripts/build_index.py) builds and searches the two
indexes, and [`scripts/answer.py`](scripts/answer.py) answers research
questions from them:

```bash
uv run python scripts/build_index.py build source_text
```

```bash
uv run python scripts/answer.py --questions 1 5 8
```

The science of reading study runs its documents through
[`scripts/workspace.py`](scripts/workspace.py), which loads one source (its
PDF, extracted text, and page images) into a separate Codex workspace and
saves the results back to the study.

## Development approach and lessons

Two coding assistants helped me build this project.

- **Claude Code** is responsible for all of the code.
- **Codex** helps with design and prompt writing.

Neither decides what I research or what the evidence means.

What has been difficult about working this way:

- Each implementation step produced the next step’s problem, and the design
  grew to absorb every one. A safeguard added for one failure became the thing
  the next step had to work around. The accumulated machinery eventually cost
  more than the failures it caught, and removing it took longer than building
  it had.
- The architecture drifted without my deciding it should. No single step chose
  to turn quotation matching into a hard acceptance gate, but it arrived there
  across many small changes that each looked reasonable at the time, and the
  direction was only visible in aggregate.
- The coding assistants did not consistently follow my instructions. I had to repeat requirements, correct assumptions, and undo changes I had not asked for. That took time and money away from the research and made supervising the assistants a substantial part of the work.

## Status and next steps

**Done**

- **Water:** all ten articles analyzed, judged, and accepted into the collection.
- **Codebook:** a draft [water codebook](studies/water/CODEBOOK.md) with three dimensions, each code illustrated with examples from the accepted analyses.
- **Research questions:** ten candidate questions a researcher would need answered to write a paper on the water question, in [`docs/PROJECT.md`](docs/PROJECT.md#research-questions).

**Next: the literacy pilot, Phase 1.** Waiting on the literacy articles and the expert's 15 questions; the plan is in [The pilot: literacy](#the-pilot-literacy). The water experiment continues after the pilot.

**Next: the water experiment**

Each approach needs its own searchable index, and each index is built the same way: break the material into pieces, turn each piece into an embedding, and store the embeddings so a question can be matched against them.

1. **Build the original-documents index (standard RAG).** Done: [`scripts/build_index.py`](scripts/build_index.py), 1,218 passages from the ten articles.
   - **Extract** the text of each article from its PDF. [`scripts/prepare_sources.py`](scripts/prepare_sources.py) already does this.
   - **Chunk** the text into passages of a set length, each labeled with its article and page.
   - **Embed** each chunk with an embedding model, which turns the passage into a vector: a list of numbers that places passages with similar meaning near each other.
   - **Index** the vectors, so that a question can be embedded the same way and matched to the nearest chunks.
2. **Build the structured-analyses index.** Done: the same script, 1,751 items from the ten articles' analyses. Split each article's close reading, claims reference, and argument evaluation into items: a step of the close reading, an entry in the claims reference, a paragraph of the argument evaluation. Label each item with its article and what kind of item it is, then embed and index the items the same way.
3. **Build the answering step.** For a question and an approach, retrieve the closest items, up to the same amount of text for every approach, and have the same model write an answer from them with the same prompt, citing a source for each claim. Record what was retrieved and what each step cost. Done: [`scripts/answer.py`](scripts/answer.py) with [`prompts/06_answer.md`](studies/water/prompts/06_answer.md); answers go to `studies/water/outputs/answers/<approach>/`.
4. **Trial run.** Answers written for questions 1, 5, and 8 with both approaches; coding them is next. Answer two or three of the questions with both approaches, code the answers with the codebook, and look closely at a few. Revise the codes, and anything in the indexes or the prompt that isn't working, before going further.
5. **Full run.** Answer all ten questions with both approaches: 20 answers.
6. **Code and compare.** Code every answer, have a second session check the coding, spot-check where the two disagree, and compare the approaches code by code and by cost.

The choices so far (chunk length, embedding model, a 4,000-token retrieved-text budget, and GPT-6.1 Sol at medium effort for the answers) are in [`docs/PROJECT.md`](docs/PROJECT.md#decisions); the budget is revisited after the trial run.

## Layout

```
├── docs/
│   ├── PROJECT.md                 the questions, current decisions, and status
│   └── ENGINEERING_DIRECTIVES.md  the coding baseline
├── studies/
│   ├── science_of_reading/        three corpora, codebooks, rubrics, prompts, results
│   └── water/                     sources, prompts, rubric, codebook, accepted analyses
├── scripts/
│   ├── run_single_source.py       water: five Codex calls per article
│   ├── workspace.py               science of reading: load a source into the Codex workspace, save its results
│   ├── build_index.py             water: index and search the articles' text and their analyses
│   ├── answer.py                  water: answer a research question from one approach's retrieved items
│   └── prepare_sources.py         extracts a PDF's text, tables, and figure crops
├── src/hitl_research_agent/       the data models and input handling prepare_sources.py uses
└── tests/
```

Earlier versions are kept as tags: `v1-final`, and `v2-final` (the A/B
experiments, the decision records, the prompt log, and the API pipeline). The
science of reading study was developed separately and is kept as `mom-research-final`.

## Setup and checks

```bash
uv sync
```

```bash
uv run pytest
```

```bash
uv run ruff check . && uv run ruff format --check .
```

```bash
uv run mypy src
```
