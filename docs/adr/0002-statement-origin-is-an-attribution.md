# ADR-0002 — `statement_origin` records an attribution, not a verification

- **Status:** Superseded by [ADR-0013](0013-lean-close-reading.md)
- **Date:** 2026-09-12
- **Landed in:** `a056be4`

## Context

An analysis is produced entirely by the model, including the parts that report
what the source says. Without a label, a reader of the JSON cannot tell a
sentence the authors wrote from a sentence the model inferred, and the second
reads with the authority of the first. With a label, there is a new and worse
risk: a field named something like `verified` or `source_says` would be read
as a guarantee that the system has checked, when nothing in the analysis call
checks anything. The model is the only thing producing the label, so the label
can only ever be the model's own report about where a statement came from.

## Decision

Every claim, statement, and methodology record carries a required
`statement_origin` of `author_stated` or `model_inferred`.

The label records **what the model asserts about provenance**. It does not
record that the assertion has been checked. `author_stated` means the model
says the source states this; it does not mean the source does. The label can
be wrong in either direction — an interpretation presented as something the
authors said, or something the authors did say recorded as the model's
inference.

Checking the label is the evaluation step's job, not the analysis step's.

## Alternatives considered

- **No label.** Every statement then reads as the source's, which is the
  failure that prompted the project.
- **A confidence score instead of a category.** A number invites being
  thresholded, and a threshold on a self-reported number is a verification
  that never happened. A two-value category is harder to mistake for a
  measurement.
- **Verify the label at write time with a text search.** Rejected: a faithful
  paraphrase is `author_stated` and appears nowhere in the document, so the
  search cannot distinguish a paraphrase that preserves the authors' meaning
  from one that drops a qualification. See [ADR-0005](0005-no-hard-quality-gates.md),
  where the same reasoning is applied to gating.

## Consequences

The schema separates author statements from model inference *as the model
reports them*, and no further. Saying the analysis separates the two describes
the schema correctly and promises nothing — which is why the README spells
this out in prose rather than leaving the field name to speak for itself.

"Invented attribution" and "omitted qualification" exist as evaluation axes
because of this decision; the separation is only as good as the model's
attributions, and the evaluation step is where they get checked.

`evidence_form` (`verbatim` / `paraphrased`) is a second and independent axis.
It describes the form of the evidence text, not who is committed to its
content. The two must not be collapsed: a faithful paraphrase is not a weaker
answer than a quotation the model was unsure of.

## Notes

Back-filled 2026-10-17. The module docstring in
`src/hitl_research_agent/models.py` states the same rule at the code. Related:
[ADR-0003](0003-application-owned-fields-stay-out-of-the-model-schema.md),
[ADR-0005](0005-no-hard-quality-gates.md).

Superseded by ADR-0013, which removes `statement_origin` from the output: in
the reading path, claims are the author's and the model's reading has its own
fields. The rule here — a label records an assertion, not a check — carries over
to `verbatim`.
