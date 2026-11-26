# Scholarly harness

Five separate Codex sessions compare baseline answers with answers informed by close reading. Run commands from the repository root. Set `OPENAI_API_KEY` in your shell; the runner passes it to Codex as `CODEX_API_KEY` for API billing instead of ChatGPT sign-in. `CODEX_API_KEY` alone also works. If both are set, `OPENAI_API_KEY` takes precedence. A missing key stops the run before any session starts. API usage is billed separately; a ChatGPT Pro subscription is not required.

## Run an article

Choose a slug from the [source list](../../data/scholarly/sources.yaml):

```bash
uv run python scripts/run_scholarly.py <slug>
```

The script runs the five steps in order and saves these files in `studies/science_of_reading/outputs/scholarly/<slug>/`:

1. `01_claims_reference.md`
2. `02_baseline_answers.md`
3. `03_close_reading.json`
4. `04_close_reading_answers.md`
5. `05_scoring.md`

Every step reads the article. Step 4 also reads the close reading; step 5 reads the claims reference and both sets of answers. The claims reference and baseline answers never see the close reading.

By default, only steps with missing output files run. Add `--only 03` to rerun the close reading. Each session receives its [prompt file](prompts/) exactly as written.
