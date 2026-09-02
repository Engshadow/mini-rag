# AGENTS — AI coding agent instructions

Purpose: Help AI coding agents be productive in this repository with minimal guesswork.

Principles
- Link, don't embed: point to existing documentation (README, code files) rather than copying it.
- Minimal by default: only include project facts an agent cannot discover automatically.
- Preserve style and tests: follow existing project patterns when adding code.

Quick references
- Project README: README.md — contains setup and run commands.
- Entrypoint: src/main.py — FastAPI app.
- Controllers: src/controllers/ — business logic and request handlers.
- Routes: src/routes/ — route wiring and nested routers.
- Helpers/config: src/helpers/config.py — env and configuration helpers.
- Requirements: requirements.txt and .env.example (copy to .env to run).

Common tasks & commands
- Create environment: `conda create -n mini-rag python=3.8` and `conda activate mini-rag`.
- Install deps: `pip install -r requirements.txt`.
- Run server: `uvicorn main:app --reload --host 0.0.0.0 --port 5000`.

Guidance for agents
- When requested to modify code, run a quick inventory (list modified files) and explain the change in the PR message.
- Avoid making unrelated style or structural changes.
- If creating new files, add a short README or comment explaining intent.

Suggested follow-ups
- Add a `.github/copilot-instructions.md` only if repository-level CI, branching, or PR conventions need to be enforced.
- Consider small skills for: running the dev server, running linters, and applying common refactorings.

Where to get help
- Primary docs: README.md

Contact/Context
- This project is a minimal RAG tutorial; many implementation decisions follow the accompanying course branches linked in README.
