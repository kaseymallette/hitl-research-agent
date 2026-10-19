from collections.abc import Sequence
from typing import Any

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage

from .inputs import InputMode, LoadedAttachment
from .models import ExtractedAnalysis, SourceDocument

SYSTEM_PROMPT = """\
You are reading a single source document. You aren't told what research \
question it will be used to answer, and there's no need to guess at one: read \
the source on its own terms, without orienting your reading toward any \
particular question, so the reading stays useful for questions no one has \
asked yet.

We'd like you to take a close reading journey through this document with us. \
Read it the way a careful reader meets it for the first time, from the opening \
to the last page, and let us travel alongside you. At each point on the way, \
you know where you've been and where you are now. Where the author is headed \
is still unfolding, so there's no need to anticipate it. Stay with what's in \
front of you, and let what came before help you understand it.

This is a close reading, not a verdict. The aim is to take in what the author \
is saying and doing, as fully and faithfully as you can. Weighing whether the \
argument ultimately holds comes later, in a separate reading, so you're free \
to simply follow along and pay attention.

As you go, record the journey in "reading_path" as a series of steps, in the \
order the document unfolds. At each step, tell us where you are and what kind \
of move the author is making. Using the language of argument helps here. Is \
the author stating a premise, or introducing evidence for a claim? Defining a \
term, giving an example, reporting a figure? Drawing an inference, or \
deducing something from what came earlier? Is an assumption at work, stated \
or left unspoken, or a value judgment? Are they qualifying a claim, comparing \
alternatives, conceding a point, answering an objection, reaching a \
conclusion, or making a recommendation? Restating something, or turning to a \
new line of discussion? If the framing reveals a perspective or a bias, \
notice it. A single step can hold more than one move.

Before you set out, take a first look through the whole document to get a \
feel for its texture: what kind of writing it is (a journal article, a \
report, an essay, a blog post) and how densely it's written. This first look \
is about the writing, not about where the argument goes, so the journey \
itself still unfolds as you read.

Let that texture set your pace. A step can take in roughly 200 to 500 words \
of the document: a medium paragraph at the small end, about a full \
single-spaced page at the large end. Where the writing is dense or technical, \
with a lot happening in a short space, stay toward the smaller end. Where it \
moves more easily, a longer stretch can be a single step. These are a sense \
of scale, not counts. Follow the natural breaks in the writing, and let a \
step run a little shorter or longer when that's where the thought ends. \
Record your first look briefly in "reading_plan": what kind of document this \
is, how densely it reads, and the pace you'll take.

Along the way, record the claims you meet as claims, with the evidence the \
author offers for them, including the figures they report. There's no need to \
sort the important ones from the rest; gather what's there.

Then reflect on where this step leaves us, given the road so far. Does it \
follow from what came before, build on it, qualify it, or start something \
new? Does the move from the last step feel earned, or does the discussion \
simply turn?

A few practices keep the record of the claims faithful.

Record each claim in the author's own words where you can, and mark it \
"verbatim" only when it reproduces their exact wording; otherwise mark it \
"paraphrased". A faithful paraphrase is never a lesser answer than a \
quotation you are unsure of.

When the author offers something in support of a claim (a figure, a study, an \
example), record it as that claim's support. A claim the author simply \
asserts needs no support listed; record it as it stands.

When support cites another work, record the citation marker exactly as \
printed, and, only if the source's own reference list has a matching entry, \
that entry exactly as written, one entry per cited work. Never invent or \
complete a reference; you are recording what the source cites, not checking \
it.

Preserve the author's strength of language. A claim stated as necessary, \
certain, or inadequate is recorded that way, not softened. Speculative, \
controversial, or weakly supported claims are recorded as fully as any other. \
When the author works through an example, keep its decisive detail, \
including any tradeoff it makes explicit.

Keep distinct claims separate, and merge only sentences that say the same \
thing. When the author restates something from earlier, note the \
restatement as a move at that step rather than recording it again.
"""


# Input-format instructions. These say only how the supplied input is laid out
# and how to record something read from an image; the analysis instructions in
# SYSTEM_PROMPT are identical in every mode, so input format stays the only
# intended difference between runs.

PDF_INPUT_INSTRUCTIONS = """\
The complete original PDF of this source is attached. No extracted text \
accompanies it, and there are no preparation annotations in this input.

Mark as "verbatim" only wording that literally appears in the document's own \
text. Content you read from a figure, chart, diagram, or an equation rendered \
as an image is not quotable text: record it as "paraphrased", and name the \
element it came from in the text itself, for example "Figure 2 shows…" or \
"Table 1 lists…". Describe what the element shows \
without presenting your reading of it as the source's printed words, and say \
so plainly where a value is unclear rather than estimating it. Such readings \
are your reading of an image, not the source's printed words."""

CROPS_INPUT_INSTRUCTIONS = """\
You are given this source's prepared text, followed by one retained image for \
each item the preparation step could not represent faithfully in that text. \
Each image is introduced by a line naming its preparation-gap identifier, its \
label in the source, and its page. The prepared text marks the same items in \
place with a labelled preparation annotation.

A preparation annotation is not source text: never quote one, and never treat \
it as the source's wording. Content you read from one of the attached images \
is likewise not quotable text: record it as "paraphrased", and name the \
element it came from in the text itself, for example "Table 1 (gap T1) \
lists…". Describe what the image shows without \
presenting your reading of it as the source's printed words, and say so \
plainly where a value is unclear rather than estimating it. Such readings are \
your reading of an image, not the source's printed words."""

INPUT_MODE_INSTRUCTIONS: dict[InputMode, str | None] = {
    "prepared_text": None,
    "prepared_text_and_crops": CROPS_INPUT_INSTRUCTIONS,
    "pdf": PDF_INPUT_INSTRUCTIONS,
}


def build_messages(
    source: SourceDocument,
    *,
    input_mode: InputMode = "prepared_text",
    attachments: Sequence[LoadedAttachment] = (),
) -> list[BaseMessage]:
    """The system prompt plus one human message carrying the supplied input.

    In the default 'prepared_text' mode the human message is the same plain
    string it has always been. The other modes add the input-format
    instructions and the attachment blocks, and the 'pdf' mode sends the PDF
    instead of the prepared text — the prepared text then serves only as the
    grounding reference and is never shown to the model.
    """
    header = (
        f"Source title: {source.provenance.source_title}\n"
        f"Source type: {source.provenance.source_type}"
    )
    instructions = INPUT_MODE_INSTRUCTIONS[input_mode]
    sections = [header]
    if instructions is not None:
        sections.append(instructions)
    if input_mode != "pdf":
        sections.append(source.text)
    framing = "\n\n".join(sections)
    if not attachments:
        return [SystemMessage(SYSTEM_PROMPT), HumanMessage(framing)]
    content: list[str | dict[Any, Any]] = [{"type": "text", "text": framing}]
    for attachment in attachments:
        content.extend(attachment.content_blocks())
    return [SystemMessage(SYSTEM_PROMPT), HumanMessage(content=content)]


# The second call: the model's own evaluation of the argument, given the article
# and the close reading from the first call. Kept apart from SYSTEM_PROMPT so the
# close reading's restraint does not hold the evaluation back (ADR-0012).

EVALUATION_PROMPT = """\
You've been given a research article, along with a close reading of it: a \
careful record of what the author states, prepared separately. Your work now \
is different. We want your own judgment of the argument as a whole: how it's \
built, whether it holds, and what shapes it. This is your interpretation, and \
it will be read as yours, so reason it through in your own voice.

Start by reading the article in its setting. Where was it published, and for \
whom? What is the paper trying to accomplish: to inform, to persuade, to \
propose, to advocate? Reading between the lines is part of the work. What the \
author emphasizes, what they pass over quickly, and what they take for granted \
can tell you as much as what they say outright.

Then lay the argument out for yourself: the premises it rests on, the \
assumptions and value judgments it brings in, the evidence behind each, and \
the conclusions and recommendations it reaches. Notice how the paper spends \
its attention. Which premises are developed at length and which are asserted \
briefly? Where are the conclusions first announced, and where are they \
actually earned?

Reason through the evidence independently rather than assuming the author's \
conclusions follow from it. Ask whether each conclusion is required by what \
has been established, merely permitted by it, or reached through assumptions \
the paper doesn't defend. Give the author's preferred solutions the same \
scrutiny as the alternatives they criticize, and consider whether different \
conclusions could reasonably follow from the same evidence. A persuasive \
narrative and a well-supported argument are not the same thing, and the \
author's intended conclusion is not the destination your reasoning has to \
reach.

Consider bias on both sides. What might shape the author's framing: their \
field, their audience, their stake in the outcome? And what is shaping yours? \
If you find the conclusion follows, ask what led you there. If you find it \
doesn't, ask what you assumed that the author may not have, and how that \
difference could explain why you see it differently.

Be willing to make a judgment. Where a passage or example from the article \
shows what you mean, point to it so a reader can follow your reasoning, but \
let the reasoning lead. You don't need to touch everything. Choose the few \
judgments that matter most about this argument and develop them fully; \
usually 1,000 to 1,500 words is enough."""

# How the article reaches the second call. Only the layout: the close-reading
# instructions about quotation and locators do not apply to an evaluation.
EVALUATION_INPUT_NOTES: dict[InputMode, str] = {
    "pdf": "The article is attached as its original PDF.",
    "prepared_text_and_crops": (
        "The article is given as prepared text, followed by one retained image for "
        "each item the preparation step could not represent in that text. Bracketed "
        "preparation annotations in the text mark those items; they are not the "
        "author's words."
    ),
    "prepared_text": "The article is given as prepared text.",
}


def build_evaluation_messages(
    source: SourceDocument,
    close_reading: ExtractedAnalysis,
    *,
    input_mode: InputMode,
    attachments: Sequence[LoadedAttachment] = (),
) -> list[BaseMessage]:
    """The evaluation prompt plus one human message carrying the article, in
    the same input mode as the close reading, and the close reading itself."""
    provenance = source.provenance
    header = [
        f"Source title: {provenance.source_title}",
        f"Source type: {provenance.source_type}",
    ]
    if provenance.publisher:
        header.append(f"Publisher: {provenance.publisher}")
    if provenance.doi:
        header.append(f"DOI: {provenance.doi}")
    sections = ["\n".join(header), EVALUATION_INPUT_NOTES[input_mode]]
    if input_mode != "pdf":
        sections.append(source.text)
    sections.append("Close reading of this article:\n" + close_reading.model_dump_json(indent=2))
    framing = "\n\n".join(sections)
    if not attachments:
        return [SystemMessage(EVALUATION_PROMPT), HumanMessage(framing)]
    content: list[str | dict[Any, Any]] = [{"type": "text", "text": framing}]
    for attachment in attachments:
        content.extend(attachment.content_blocks())
    return [SystemMessage(EVALUATION_PROMPT), HumanMessage(content=content)]


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
