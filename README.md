# looop-researcher

Local automatic research loops over codebases.

## Setup

This project is managed with `uv` and targets Python 3.11.

```bash
uv sync --dev
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run a quick environment check:

```bash
uv run python scripts/check_env.py
```

Run tests and linting:

```bash
uv run pytest
uv run ruff check .
```

## Ollama

Ollama is expected to run locally as the model server:

```bash
ollama serve
```

In another terminal, pull a model:

```bash
ollama pull llama3.1
```

The Python package `ollama` is included so research-loop code can call the local Ollama API directly.
