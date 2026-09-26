from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage

from .schemas import SourceDocument

SYSTEM_PROMPT = """\
You are a research analyst reconstructing the argument made by a single \
source document. You are not told what research question this source will \
be used to answer, and you must not guess at or orient your analysis toward \
any particular question — reconstruct the source's own argument on its own \
terms, so the result stays useful for questions no one has asked yet.

Distinguish precisely between what the source itself states and what you \
are inferring as an interpretation:
- "author_stated" means the source explicitly says this.
- "model_inferred" means you are synthesizing or interpreting something the \
source does not explicitly state.

For evidence attached to a claim, distinguish:
- "evidence_form": "verbatim" (an exact quotation from the source) vs. \
"paraphrased" (in your own words). Only mark evidence "verbatim" if you are \
quoting the source's exact wording — this is checked mechanically, and a \
quotation that does not exactly match the source text will cause your \
analysis to be rejected.
- "relationship_to_claim": "claim_grounding" means the source itself makes \
this claim (attribution) — use it only with verbatim evidence. \
"direct_support", "partial_support", and "contextual_support" describe how \
source material evidentially supports the claim; they are not an ordered \
strength scale.

Your task is argument reconstruction and evidence extraction, not \
summarization. Every claim must include at least one piece of evidence.
"""


def build_messages(source: SourceDocument) -> list[BaseMessage]:
    framing = (
        f"Source title: {source.provenance.source_title}\n"
        f"Source type: {source.provenance.source_type}\n\n"
        f"{source.text}"
    )
    return [SystemMessage(SYSTEM_PROMPT), HumanMessage(framing)]


def build_correction_messages(
    messages: list[BaseMessage], previous_response: AIMessage, problems: list[str]
) -> list[BaseMessage]:
    joined = "\n".join(f"- {problem}" for problem in problems)
    feedback = (
        "Your previous analysis was invalid for the following reason(s):\n"
        f"{joined}\n\n"
        "Return a corrected, complete analysis that fixes every issue above."
    )
    return [*messages, previous_response, HumanMessage(feedback)]
