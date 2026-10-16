from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str | None = None
    openai_model: str = "gpt-6-astra"
    openai_reasoning_effort: str = "low"
    max_source_characters: int = 200_000
    # Sent as the Responses API's max_output_tokens when set. Unset by default,
    # so ordinary runs are unchanged; a pilot run sets it to bound its own cost.
    max_output_tokens: int | None = None
    # Retries performed inside the OpenAI client, which the pipeline cannot see
    # or record. None leaves the client's own default (2) in place; 0 makes each
    # analysis attempt exactly one HTTP request.
    openai_max_retries: int | None = None
