# Literacy pilot

The pilot compares traditional RAG (searching the articles' text) with structured RAG (searching each article's close reading, claims reference, and argument evaluation) on three literacy articles, judged by a literacy education professor. It follows the standard benchmark methods: TREC's pooled relevance judgments and metrics for retrieval, and the TREC 2024 RAG Track's nugget and support evaluation for the answers.

*Planned. The articles are in `data/` (local only, publisher-copyrighted); the candidate questions await approval.*

## Roles

| Who | Does |
| --- | --- |
| The expert | Approves the 15 questions and their relevance criteria, and makes every judgment |
| Kasey | Runs both approaches and computes the scores |
| All three | Review the results |

The expert judges without seeing which approach retrieved a piece, its rank, or any score.

## Phase 1: the expert judges

### 1. Questions (TREC topics)

Each question is a TREC-style topic: an ID, the question, and a **narrative**, a short statement of what makes a piece relevant, approved before any judging. In TREC the assessor owns the topic; here the expert approves the drafted question and narrative, so they are hers.

Five questions of each kind:

- **Explicit:** the answer is stated in one place in one article.
- **Conceptual:** the answer needs an idea explained, possibly spread across an article.
- **Synthesis:** the answer needs more than one article.

The candidates, awaiting approval:

| ID | Question |
| --- | --- |
| E01 | What criteria were used to select the middle schools participating in the survey of accomplished educators? |
| E02 | What assessment instruments were used to develop individualized literacy intervention plans for adolescents? |
| E03 | What responsibilities did the preservice teachers undertake in their roles as teacher-researchers? |
| E04 | What data sources were collected during the academic year following the summer literacy intervention? |
| E05 | How were the quantitative and qualitative survey responses analyzed in the study of middle-level educators? |
| C01 | How does the belief that effort determines academic success obscure structural inequities? |
| C02 | How do interpersonal relationships influence adolescents' engagement with literacy learning? |
| C03 | To what extent do educators privilege conventional literacy practices over broader forms of communication? |
| C04 | How do researchers' theoretical perspectives shape their interpretations of teacher knowledge? |
| C05 | How does the separation of academic disciplines constrain opportunities for literacy development? |
| S01 | What evidence challenges an exclusively skills-based conceptualization of literacy learning? |
| S02 | How do social and cultural contexts shape understandings of literacy? |
| S03 | What tensions exist between contemporary literacy scholarship and educators' beliefs or practices? |
| S04 | How do researchers integrate different analytical approaches to develop more comprehensive understandings of literacy? |
| S05 | What implications do the studies have for the preparation of literacy educators? |

### 2. Runs

Each article gets the single-source analysis (close reading, claims reference, argument evaluation), and both indexes are built, with the water study's settings: article text in passages of up to 200 tokens, analysis items of about the same size, every piece with a unique ID. Each approach returns a ranked list of its top 10 pieces for each question, saved in TREC run format.

### 3. Pooling and judging

The two top-10 lists for a question are merged into one **pool** (depth-10 pooling, TREC's standard). The two approaches search different pieces, so each pool has 20, and the 15 questions about 300 in all. The pool is shuffled and shown without approach, rank, or score.

The expert grades each piece against the question's narrative:

| Grade | Meaning |
| --- | --- |
| 2 | Directly relevant: substantive evidence addressing the question |
| 1 | Partially relevant: supporting evidence or meaningful context |
| 0 | Not relevant |

The grades are saved as TREC qrels. As in TREC, a piece that was never retrieved is unjudged and counts as not relevant.

Two limits, stated with the results:

- **Judging after retrieval.** Judging every piece before retrieval would give true recall, but for both approaches that is about 800 pieces × 15 questions, some 12,000 judgments. Pooling is what TREC does instead: the expert sees only what was retrieved, blind to who retrieved it.
- **Not fully blind.** A close-reading or claims-reference item reads differently from article text, so the kind of piece shows which approach found it, even with the labels removed.

### 4. Retrieval scores

Computed with trec_eval's definitions, per question, then averaged over all 15 and over each kind:

- **nDCG@10** (primary, as in BEIR): whether the most relevant pieces come first, using the grades 0, 1, 2 as gains.
- **Precision@10**: the share of the top 10 that is relevant.
- **Recall@10**: the share of the pool's relevant pieces that this approach found. It is recall against what the two approaches found together, not against every relevant piece in the articles.
- **F1@10**: the balance of the two.

Precision, recall, and F1 are reported twice: **strict** (only grade 2 counts as relevant; trec_eval `-l 2`) and **inclusive** (grades 1 and 2; `-l 1`).

### 5. Answers (TREC 2024 RAG)

Each question is answered from each approach's retrieved pieces, with the same model, prompt, and 4,000-token budget as the water study, citing the pieces it uses: 30 answers. They are judged the way the TREC 2024 RAG Track judges answers:

- **Nuggets.** For each question, a list of the points a good answer should contain, drawn from the pieces graded relevant and approved by the expert, each marked *vital* or *okay*. Each answer is checked for each nugget: supported, partly supported, or missing. The score is **nugget recall**, for vital nuggets and for all.
- **Support.** For each cited sentence in an answer: does the cited piece fully support it, partly, or not at all? The score is **support precision**: the share of cited sentences their citations support. This is the attribution check: an answer that cites a piece for something it doesn't say is caught here.

### 6. Compare

The two approaches side by side, overall and by kind of question, on retrieval (nDCG@10, precision, recall, F1) and on answers (nugget recall, support precision). Fifteen questions is a small benchmark (TREC tracks use about 50), so results are reported per question as well as averaged, and differences are described, not tested for significance.

## Phase 2: generated questions (after Phase 1's results)

A model writes one question for each piece, a question that piece answers, for all four kinds of piece. Each question's correct answer is the piece it was written from. Searching with each question gives **recall@5, recall@10**, and **MRR** (how high the piece ranks on average, from 1 to 0) for each approach. If the generated questions rank the approaches the way the expert's judgments do, they can stand in where there is no expert, as in the water study.

## Sources for the methods

- Depth-k pooling and unjudged-as-nonrelevant: Zobel, "How reliable are the results of large-scale information retrieval experiments?" (SIGIR 1998); Lu, Moffat, and Culpepper, ["The effect of pooling and evaluation depth on IR metrics"](https://people.eng.unimelb.edu.au/ammoffat/abstracts/lmc16irj.html) (2016).
- Assessor disagreement leaves system rankings stable: Voorhees, ["Variations in relevance judgments and the measurement of retrieval effectiveness"](https://www.nist.gov/node/710491) (2000).
- Strict and inclusive thresholds with trec_eval `-l`: the [TREC 2019 Deep Learning Track](https://trec.nist.gov/data/deep2019.html) guidance.
- nDCG@10 as the primary metric: Thakur et al., ["BEIR"](https://arxiv.org/abs/2104.08663) (2021).
- Nugget evaluation: Pradeep et al., ["Initial nugget evaluation results for the TREC 2024 RAG Track"](https://arxiv.org/abs/2411.09607) (2024).
- Support evaluation: ["Support evaluation for the TREC 2024 RAG Track: comparing human versus LLM judges"](https://arxiv.org/abs/2504.15205) (2025).
