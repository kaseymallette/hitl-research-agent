# ADR-0015 — Phase 1 runs as three experiments, one per article

- **Status:** Accepted
- **Date:** 2026-10-20
- **Landed in:** not yet committed

## Context

[ADR-0009](0009-phase-1-matrix-three-configurations-three-articles.md) set
Phase 1 as one matrix: three articles, each analyzed by three model
configurations (GPT-6.1 Sol medium, Sol high, GPT-6 Astra low) through two
input methods (the full PDF, or prepared text plus crops), for 18 runs.

The first article, Barnett, has run all six of its cells under the current
design ([ADR-0013](0013-lean-close-reading.md)). Three things came out of it:

- **Astra low cost about four times as much as Sol** — $1.17 and $1.29 a run
  against $0.28–0.39 — and recorded fewer claims (84–93 against 109–135),
  with no advantage in the analyses that I could see.
- **The two input methods produced analyses of about the same quality.** The
  prepared text needed manual fixes on both articles prepared so far — a
  front-matter break in Barnett, nine caption and footnote breaks in kanbur —
  and preparation kept no crops of kanbur's figures, so the text arm never
  sees its result plots.
- **A new question:** does the API do anything the ChatGPT app cannot? I use
  the app with a subscription. If the app reads and reasons as well, the
  API's value is everything around the model — enforced structure, run
  records, exact cost, repeatable settings, and scale — rather than the
  reading itself.

Running the remaining two articles through the same 18-run matrix would spend
most of its cost on Astra and on an input comparison Barnett has already made
once, and could not answer the app question at all.

## Decision

**Phase 1 is three experiments, one per article, each designed for what is
still open.**

| Experiment | Article | Design | Runs |
| --- | --- | --- | --- |
| 1 | Barnett | 3 model configurations × 2 input methods (ADR-0009) | 6, complete |
| 2 | kanbur | PDF only: 2 efforts × 3 ways of running | 6 |
| 3 | lei | designed after Experiment 2 | to be decided |

**Experiment 2** compares ways of running the same two prompts, with the PDF
as the input throughout:

| | API, GPT-6.1 Sol | App, GPT-6, Temporary Chat | App, GPT-6, regular chat with memory |
| --- | --- | --- | --- |
| **Medium effort** | 1 | 1 | 1 |
| **High effort** | 1 | 1 | 1 |

- **Astra low is dropped** from Experiment 2 on, for its cost, with no
  advantage shown on Barnett.
- **Prepared text plus crops sits out Experiment 2.** Lei, at 60 pages, is
  where the input method matters most for cost, so Experiment 3 is the likely
  place to compare it again — perhaps PDF against text plus crops on two
  models. [ADR-0008](0008-compare-pdf-against-prepared-text.md) stays open, and
  `prepare_sources.py` stays.

**The app runs follow a fixed procedure**, so the only intended difference from
an API run is the way it is run:

1. **Call 1, the close reading:** a new chat at the stated model and effort,
   with the article's PDF attached and one message holding the source header
   (title and type), the PDF layout instructions, `SYSTEM_PROMPT`, and one
   addition: a format instruction asking for JSON in the shape of the close
   reading schema. The API enforces that schema separately and never states it
   in words; the app cannot enforce one, so it is asked for. The instruction is
   in [docs/PROMPTS.md](../PROMPTS.md).
2. **Call 2, the argument evaluation:** a second new chat, so it does not
   inherit call 1's instructions, as the API's second call does not. The PDF
   attached, and one message holding the source header (title, type,
   publisher, DOI), the PDF note, `EVALUATION_PROMPT`, and call 1's close
   reading.
3. **Temporary Chat** is the app with memory and past chats unavailable to the
   model. **Regular chat** is the app as I normally use it, memory on.

App results are saved by hand beside the API's, in folders named
`chat__gpt-6-<effort>-temp` and `chat__gpt-6-<effort>-memory`: the close
reading as `analysis.json`, as returned, and the evaluation as
`argument_evaluation.md`, as returned.

**My notes on each article come first.** I write them before reading any
output from either the API or the app, so they stay an independent reading to
compare both against.

## Alternatives considered

- **Keep the 18-run matrix.** Repeats a comparison Barnett has made once,
  spends most of its cost on Astra, and cannot test the app.
- **Drop the text arm for good** and remove `prepare_sources.py`. That would
  settle ADR-0008 on one article. Lei is the stronger test of whether
  preparation pays off, so the decision waits for it.
- **Test the app on Barnett.** An app run on Barnett was tried and discarded:
  it was not in a Temporary Chat, and I had discussed Barnett with ChatGPT, so
  memory could have shaped its reading. Kanbur has not come up with it.

## Consequences

**API against app compares two models as well as two ways of running.** The
API runs use GPT-6.1 Sol; the app offers GPT-6. A difference between them may
come from the model, from the app's own hidden instructions, or from how each
handles the PDF. Temporary Chat against regular chat has no such confound: the
same model in the same app, with memory the only difference.

**The app gives no usage or cost.** It is a subscription, and the app reports
no tokens, so app runs have no run record. Their cost is the subscription and
the time spent running them by hand.

**Memory can carry more than earlier discussion of an article.** What the app
remembers of how I read or what I think may shape its reading even of an
article it has never seen. That is part of what the memory-on run measures.

**ADR-0009's matrix is superseded** for kanbur and lei. Barnett's six runs stand
as Experiment 1, under ADR-0013's prompts.

**The prompts now live in one current document.** [docs/PROMPTS.md](../PROMPTS.md)
holds both system prompts, the input instructions, and the app's format
instruction, and a test keeps it in step with the code. The ADRs keep each
version as it was decided.

## Notes

Supersedes ADR-0009's matrix for Experiments 2 and 3 only. ADR-0008 remains
open.
