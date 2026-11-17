# Hermes Local — AI Agent Container

Запуск Hermes Agent + Claude Code + Codex в изолированном Docker-окружении на macOS (Apple Silicon / Intel).  

## Быстрый старт

```bash
# 1. Скопируйте и заполните ключи
cp .env.example .env
# → отредактируйте .env, вставьте свои API ключи

# 2. Соберите и запустите
docker compose up --build

# → откроется Hermes в интерактивном режиме
```

## Структура

```
├── Dockerfile          — Python + Hermes + Claude Code + Codex
├── docker-compose.yml  — volumes, env, tty
├── entrypoint.sh       — проверка ключей, запуск
├── .env.example        — шаблон для API ключей
├── .gitignore
└── README.md
```

## Использование

**Интерактивный режим (рекомендуется):**
```bash
docker compose up --build
```

**Разовая команда:**
```bash
docker compose run --rm agent hermes chat -q "What is the capital of France?"
```

**Запуск Claude Code:**
```bash
docker compose run --rm agent claude
```

**Оболочка:**
```bash
docker compose run --rm agent bash
```

## Безопасность

- Контейнер видит **только** смонтированные директории (по умолчанию `./workspace:/workspace`)
- API-ключи — в отдельном `.env`, не в `config.yaml`
- `~/.ssh`, `~/.aws`, `~/Documents` **не смонтированы** — агенты к ним не имеют доступа
- Для доступа к конкретному проекту: добавьте volume в `docker-compose.yml`:
  ```yaml
  volumes:
    - ~/projects/my-app:/workspace/my-app
  ```

## Зависимости

- [OrbStack](https://orbstack.dev) (рекомендуется) или Docker Desktop
- Make, git (необязательно)

## Сборка с нуля

```bash
docker compose build --no-cache   # полная пересборка
docker compose up                  # запуск
```

## Что внутри контейнера

| Инструмент | Команда | Источник |
|---|---|---|
| Hermes Agent | `hermes` | Официальный установщик |
| Claude Code | `claude` | npm-пакет |
| OpenAI Codex | `codex` | npm-пакет |

Все инструменты работают внутри контейнера с изолированным окружением. Хост-система не загрязняется зависимостями.