"""
Фильтр алертов: из потока событий оставляет только critical.

Никаких агентов и LLM — обычный filter по полю level.

Запуск:
    python filter_alerts.py [events.json]
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "events.json")
    events = json.loads(path.read_text(encoding="utf-8"))

    critical = [e for e in events if e.get("level", "").lower() == "critical"]

    for e in critical:
        print(f"[CRITICAL] {e['event']}")

    print(f"summary: критичных {len(critical)}")


if __name__ == "__main__":
    main()
