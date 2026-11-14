# Адвокат диявола

Вебзастосунок, який критикує ваші тези за допомогою локальної моделі через Ollama.

## Що потрібно

1. **Ollama** — [ollama.com/download](https://ollama.com/download)
2. **Модель**: `ollama pull qwen3:1.7b-q8_0`
3. **Браузер** (Chrome, Firefox, Edge)

## Як запустити

1. Переконайтеся, що Ollama запущено (іконка в треї).
2. Відкрийте `index.html` у браузері (подвійний клік).
3. Введіть тезу → «Атакувати».

**Якщо браузер блокує запит (CORS):**
Запустіть Ollama з дозволом CORS (у PowerShell):
```powershell
$env:OLLAMA_ORIGINS = "*"
ollama serve