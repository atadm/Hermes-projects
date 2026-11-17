#!/bin/bash
set -e

echo "╔═══════════════════════════════════════════╗"
echo "║     Hermes + Claude Code + Codex         ║"
echo "║     Контейнер для AI-агентов             ║"
echo "╚═══════════════════════════════════════════╝"
echo ""

# Переменные окружения
echo "── Проверка API ключей ──"
[ -n "$OPENAI_API_KEY" ]      && echo "  ✓ OPENAI_API_KEY"      || echo "  ✗ OPENAI_API_KEY (не задан)"
[ -n "$ANTHROPIC_API_KEY" ]   && echo "  ✓ ANTHROPIC_API_KEY"   || echo "  ✗ ANTHROPIC_API_KEY (не задан)"
[ -n "$OPENROUTER_API_KEY" ]  && echo "  ✓ OPENROUTER_API_KEY"  || echo "  ✗ OPENROUTER_API_KEY (не задан)"
echo ""

echo "── Доступные команды ──"
echo "  hermes                — запустить Hermes"
echo "  hermes chat -q '...'  — разовый запрос"
echo "  claude                — Claude Code"
echo "  codex                 — OpenAI Codex"
echo "  bash                  — оболочка"
echo ""

# Запуск
if [ $# -eq 0 ]; then
    exec hermes
else
    exec "$@"
fi