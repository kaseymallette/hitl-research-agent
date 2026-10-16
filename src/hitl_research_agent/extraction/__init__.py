from .annotations import find_annotations
from .attachments import (
    Attachment,
    InputMode,
    LoadedAttachment,
    load_attachment,
    validate_attachments,
)
from .attempts import AttemptRecord, AttemptUsage
from .errors import (
    SourceAnalysisError,
    SourceAnalysisExtractionError,
    SourceAnalysisIncompleteError,
    SourceAnalysisRefusedError,
    SourceAnalysisValidationError,
    SourceTooLargeError,
)
from .pipeline import analyze_source
from .schemas import (
    ANALYSIS_SCOPE,
    ANALYSIS_SCOPE_BY_INPUT_MODE,
    ANALYSIS_SCOPE_PDF,
    ANALYSIS_SCOPE_TEXT_AND_CROPS,
    AnalysisResult,
    ExtractedAnalysis,
    ExtractedClaim,
    ExtractedEvidence,
    PreparationGap,
    SourceDocument,
)

__all__ = [
    "ANALYSIS_SCOPE",
    "ANALYSIS_SCOPE_BY_INPUT_MODE",
    "ANALYSIS_SCOPE_PDF",
    "ANALYSIS_SCOPE_TEXT_AND_CROPS",
    "AnalysisResult",
    "Attachment",
    "AttemptRecord",
    "AttemptUsage",
    "InputMode",
    "LoadedAttachment",
    "ExtractedAnalysis",
    "ExtractedClaim",
    "ExtractedEvidence",
    "PreparationGap",
    "SourceAnalysisError",
    "SourceAnalysisExtractionError",
    "SourceAnalysisIncompleteError",
    "SourceAnalysisRefusedError",
    "SourceAnalysisValidationError",
    "SourceDocument",
    "SourceTooLargeError",
    "analyze_source",
    "find_annotations",
    "load_attachment",
    "validate_attachments",
]
