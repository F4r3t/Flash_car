import json
from pathlib import Path


SAVE_FILE = Path("save.json")


def load_best_score() -> int:
    if not SAVE_FILE.exists():
        return 0

    try:
        data = json.loads(SAVE_FILE.read_text(encoding="utf-8"))
        return int(data.get("best_score", 0))
    except (json.JSONDecodeError, ValueError, TypeError):
        return 0


def save_best_score(score: int) -> None:
    current_best = load_best_score()
    if score > current_best:
        SAVE_FILE.write_text(
            json.dumps({"best_score": score}, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )