from datetime import UTC, datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from hitl_research_agent.models.provenance import Provenance


def _provenance(**overrides: object) -> Provenance:
    defaults: dict[str, object] = dict(
        source_title="Title",
        source_type="peer_reviewed_paper",
        retrieved_at=datetime.now(UTC),
    )
    defaults.update(overrides)
    return Provenance(**defaults)


def test_source_id_defaults_to_unique_uuid() -> None:
    a = _provenance()
    b = _provenance()
    assert a.source_id != b.source_id


def test_source_id_can_be_reused_across_reanalysis() -> None:
    shared_id = uuid4()
    first = _provenance(source_id=shared_id)
    second = _provenance(source_id=shared_id)
    assert first.source_id == second.source_id


@pytest.mark.parametrize(
    "value", ["research_institute_report", "technical_document", "government_policy"]
)
def test_new_source_type_values_accepted(value: str) -> None:
    _provenance(source_type=value)


def test_doi_and_publisher_are_optional() -> None:
    p = _provenance()
    assert p.doi is None
    assert p.publisher is None


def test_doi_and_publisher_reject_whitespace_only() -> None:
    with pytest.raises(ValidationError):
        _provenance(doi="   ")
    with pytest.raises(ValidationError):
        _provenance(publisher="   ")


def test_retrieved_at_requires_timezone() -> None:
    with pytest.raises(ValidationError):
        _provenance(retrieved_at=datetime.now())


def test_retrieved_at_is_timezone_aware() -> None:
    p = _provenance()
    assert p.retrieved_at.utcoffset() is not None


def test_source_authors_list_defaults_are_independent() -> None:
    a = _provenance()
    b = _provenance()
    a.source_authors.append("Someone")
    assert b.source_authors == []
