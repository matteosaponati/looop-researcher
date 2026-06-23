# 2026-06-23 Gemma 4 Modelfile

- Added an Ollama Modelfile for a local Gemma 4 E4B research-loop assistant.
- Pinned the base model to `gemma4:e4b-mlx` for Apple Silicon.
- Kept `num_ctx 65536` for a 24 GB MacBook Pro.
- Explicitly configured every current Ollama model option available through `PARAMETER`.
- Used Gemma 4 sampling recommendations and build/run usage comments.
- Removed prompt-shaping instructions: no `SYSTEM`, `TEMPLATE`, or `MESSAGE` entries are included.
- Added `module.json` with an Ollama provider entry for PI using the created model id `gemma4-researcher`.
