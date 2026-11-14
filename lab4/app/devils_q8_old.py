import time
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="local")

SYSTEM_PROMPT = (
    "Ти — «Адвокат диявола». Користувач дає тобі тезу, ідею чи виправдання. "
    "Твоє завдання — безжально, але дотепно розкрити слабке місце в логіці. "
    "Структура відповіді: (1) Слабке місце — одне речення. "
    "(2) Найгірший сценарій — 1–2 речення, що станеться, якщо так зробити. "
    "(3) Контр-аргумент — один жорсткий, конкретний, без води. "
    "Пиши українською (або мовою тези), максимум 120 слів. Без вітань і моралізаторства."
)

PROMPTS = [
    "Я почну робити лабу завтра вранці, бо зараз мозок вже не варить",
    "Я перепишу весь код лаби з нуля за одну ніч перед дедлайном — так буде чистіше",
    "Мені не потрібно тестувати застосунок, він же простий",
    "Я використаю модель на 8B, бо вона розумніша, і хай собі повільно працює",
    "Я не робитиму README, викладач і так зрозуміє, як запускати",
    "Я додам у застосунок 10 фіч, щоб він виглядав серйозніше",
    "Я проігнорую поради з лаби й зроблю по-своєму, бо я краще знаю",
    "I'll just copy a solution from GitHub and tweak it a bit — nobody will notice",
    "Я вже вклав 3 дні в цю архітектуру, тому не буду її міняти, навіть якщо вона не працює",
    "Я просто не буду здавати лабу — це ж лише одна оцінка",
]

MODEL = "qwen3:1.7b-q8_0"
LABEL = "after1"

results = []
for i, prompt in enumerate(PROMPTS, 1):
    start = time.perf_counter()
    r = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300,
        temperature=0.3,
        extra_body={"reasoning_effort": "none"},
    )
    elapsed = time.perf_counter() - start
    answer = r.choices[0].message.content.strip()
    results.append((i, prompt, answer, elapsed))
    print(f"\n=== {i}. {prompt}  ({elapsed:.1f} с) ===")
    print(answer)

with open(f"devils_{LABEL}.txt", "w", encoding="utf-8") as f:
    for i, prompt, answer, elapsed in results:
        f.write(f"### {i}. {prompt}\n({elapsed:.1f} с)\n{answer}\n\n")
print(f"\nЗбережено у devils_{LABEL}.txt")