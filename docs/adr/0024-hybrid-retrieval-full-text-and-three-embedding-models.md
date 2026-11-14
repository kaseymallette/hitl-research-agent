# ADR-0024 — Retrieval is hybrid: full-text search and three local embedding models, compared on the same queries

- **Status:** Accepted
- **Date:** 2026-11-12
- **Landed in:** not yet committed

## Context

[ADR-0023](0023-synthesis-retrieves-from-a-store-of-the-accepted-articles.md)
gave the store full-text search and set embeddings aside as not shown to
retrieve better. But the articles describe the same things in different
words — withdrawal and consumption, evaporative cooling and cooling towers,
WUE and litres per kilowatt-hour — and full-text search finds only the words
it is given. Similarity is not agreement either: two claims can sit close
together in embedding space while measuring different quantities.

The synthesis session runs in Codex, whose `workspace-write` sandbox has no
network access, so whatever embeds a query has to run locally. The machine
has 16 GB of RAM. The items range from one-sentence claims to sections of a
claims reference or argument evaluation that run to several hundred words.
Which embedding model retrieves best for these items was not known.

## Decision

**The store holds a vector for every item from each of three local embedding
models, beside its full-text index, and the query script searches by text, by
embedding, or both.**

| Model | Parameters | Input limit |
| --- | --- | --- |
| `BAAI/bge-m3` | about 570M | 8,192 tokens |
| `Qwen/Qwen3-Embedding-0.6B` | about 600M | about 32K tokens |
| `sentence-transformers/all-MiniLM-L6-v2` | about 22M | 256 tokens |

- The builder embeds every item with each model, run locally through
  sentence-transformers. Each model's vectors are their own table in the same
  SQLite database, keyed by item ID. There is no vector database: search
  compares the query's vector against every stored one.
- The store build records each model's ID and revision alongside the hash of
  its input files.
- The query script takes `--method text`, `embedding`, or `hybrid`, and
  `--model` for the embedding. Hybrid merges the text and embedding rankings by
  reciprocal rank fusion. Synthesis uses hybrid with bge-m3 by default. Every
  result still names its kind and source.
- The query script loads one model from the local cache in offline mode, so it
  works inside the Codex sandbox; the models are downloaded once, outside it.
- Every query is logged with its method and model. The logged queries are the
  test set: each is rerun as full-text alone and with each model alone and in
  hybrid, seven ways in all, so no research question is needed to evaluate
  retrieval ([ADR-0006](0006-analysis-and-synthesis-never-receive-the-question.md)).
  The winner becomes the default, recorded in a note here.
- Retrieval finds candidates. Whether retrieved claims agree, disagree, or
  address different things is for synthesis to decide.
- PyTorch and sentence-transformers are their own `uv` dependency group, so
  the main install and CI stay light; tests use a stub embedder.

## Alternatives considered

- **Full-text search only, as ADR-0023 had it.** The synthesis model can
  rewrite its queries, which covers some of the vocabulary gap, but not a
  term it does not think to try.
- **One embedding model, chosen up front.** Nothing showed which would
  retrieve best here; storing all three makes the comparison a flag.
- **Gemma 4 12B.** A generative model: vectors taken from its hidden states
  usually retrieve worse than a model trained for embeddings, and at 4-bit it
  needs about 7 GB, loaded for each query alongside Codex.
- **EmbeddingGemma, all-mpnet-base-v2, bge-small-en-v1.5.** Considered;
  three models already span a long-input encoder, a model built from a
  language model, and a very small baseline.
- **Qwen3-Embedding 4B or 8B.** Too large to load beside Codex on 16 GB.
- **An embeddings API.** Unreachable from the Codex sandbox, and billed.
- **A vector database.** A few thousand items need no index beyond a table.
- **Embeddings later, after an experiment.** Building them now makes the
  comparison a flag on logged queries rather than a second build.

## Consequences

**A query can find a claim that uses none of its words**, and can also
surface claims that only look related; synthesis and its judgment are where
that is sorted out.

**The store build gets heavier.** Embedding every item three times needs
PyTorch and about 3 GB of models, and takes minutes rather than seconds. It is
still local, free, and rebuilt from committed files.

**all-MiniLM-L6-v2 reads only the start of a long item.** Its 256-token limit
cuts off longer sections before they are embedded; full-text search still
covers them. That is part of what the comparison measures.

**The models are dependencies to pin.** A different model or revision changes
the vectors, so the store build records them and a change means a rebuild.

**Which method and model retrieve best is an open result.** Hybrid with bge-m3
is the default until the logged queries show otherwise.

## Notes

Amends the retrieval in
[ADR-0023](0023-synthesis-retrieves-from-a-store-of-the-accepted-articles.md),
which had full-text search only. The rest of ADR-0023 stands.

The sizes and input limits above are as the models were known when this was
decided; each model's revision on Hugging Face is pinned, and its card
checked, when the builder is written.
