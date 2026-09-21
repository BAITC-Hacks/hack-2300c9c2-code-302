"""
Классификатор обращений: поток сообщений -> категория -> черновик ответа.

Правила заданы ключевыми словами (без вызова LLM — быстрее и не требует ключа).
Категории: справка / жалоба / другое.

Запуск:
    python classify_messages.py [messages.txt]
"""

import sys
from pathlib import Path

COMPLAINT_WORDS = [
    "очеред", "холодн", "пропал", "не работает", "плохо",
    "проблема", "сломал", "жалоб",
]

INFO_REQUEST_WORDS = [
    "как получить", "справк", "где", "какие документы",
    "во сколько", "когда работает",
]

DRAFT_REPLIES = {
    "жалоба": "Спасибо, что сообщили — передаём информацию ответственной службе, ситуацию проверят в ближайшее время.",
    "справка": "Отвечаем на ваш вопрос ниже, при необходимости уточните детали в деканате/АХЧ.",
    "другое": "Ваше обращение принято в обработку, с вами свяжутся для уточнения деталей.",
}


def classify(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in COMPLAINT_WORDS):
        return "жалоба"
    if any(word in lowered for word in INFO_REQUEST_WORDS):
        return "справка"
    return "другое"


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "messages.txt")
    messages = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    for i, message in enumerate(messages, start=1):
        category = classify(message)
        reply = DRAFT_REPLIES[category]
        print(f"{i}. {message}")
        print(f"   категория: {category}")
        print(f"   черновик ответа: {reply}")
        print()


if __name__ == "__main__":
    main()
