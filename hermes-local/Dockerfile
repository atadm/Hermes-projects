# Context
FROM python:3.13-slim-bookworm AS base

RUN apt-get update -qq && apt-get install -y -qq \
    curl git npm nodejs tmux \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# ── Hermes Agent ──────────────────────────────────────────
RUN curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
ENV PATH="${PATH}:/root/.local/bin"

# ── Claude Code ───────────────────────────────────────────
RUN npm install -g @anthropic-ai/claude-code

# ── Codex (OpenAI) ───────────────────────────────────────
RUN npm install -g openai-codex

# ── Entrypoint ────────────────────────────────────────────
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]