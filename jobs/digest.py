"""Daily digest over data/items.json."""

import datetime as dt
import json
import os
import sys
from collections import Counter
from pathlib import Path

DATA_DIR = Path(os.environ.get("DATA_DIR", Path(__file__).resolve().parents[1] / "data"))


def load_items() -> list[dict]:
    return json.loads((DATA_DIR / "items.json").read_text())["items"]


def build_digest(date: dt.date) -> dict:
    items = [item for item in load_items() if item["date"] == date.isoformat()]
    by_category = Counter(item["category"] for item in items)
    top = sorted(items, key=lambda item: item["score"], reverse=True)[:3]
    return {
        "date": date.isoformat(),
        "total_items": len(items),
        "by_category": dict(sorted(by_category.items())),
        "top_items": [{"title": item["title"], "score": item["score"]} for item in top],
    }


def main(argv: list[str]) -> None:
    if argv:
        date = dt.date.fromisoformat(argv[0])
    else:
        date = max(dt.date.fromisoformat(item["date"]) for item in load_items())
    print(json.dumps(build_digest(date), indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
