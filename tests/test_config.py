import pytest

from hitl_research_agent.config import Settings


def test_package_imports() -> None:
    import hitl_research_agent  # noqa: F401


def test_settings_constructs_without_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    settings = Settings(_env_file=None)
    assert settings.openai_api_key is None


def test_settings_loads_api_key_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    settings = Settings(_env_file=None)
    assert settings.openai_api_key == "test-key"


def test_settings_phase_2_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    monkeypatch.delenv("OPENAI_REASONING_EFFORT", raising=False)
    monkeypatch.delenv("MAX_SOURCE_CHARACTERS", raising=False)
    settings = Settings(_env_file=None)
    assert settings.openai_model == "gpt-6-astra"
    assert settings.openai_reasoning_effort == "low"
    assert settings.max_source_characters == 200_000


def test_settings_phase_2_fields_are_overridable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_MODEL", "gpt-6-sol")
    monkeypatch.setenv("OPENAI_REASONING_EFFORT", "high")
    monkeypatch.setenv("MAX_SOURCE_CHARACTERS", "50000")
    settings = Settings(_env_file=None)
    assert settings.openai_model == "gpt-6-sol"
    assert settings.openai_reasoning_effort == "high"
    assert settings.max_source_characters == 50_000
