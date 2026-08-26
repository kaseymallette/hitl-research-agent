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
