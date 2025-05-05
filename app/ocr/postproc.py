import re
import rapidfuzz
from .config import LEXICON_PATH

with open(LEXICON_PATH) as f:
    CANON = [l.strip().upper() for l in f]


def tokenise(line: str) -> tuple[str | None, float | None]:
    # extract price at end
    m = re.search(r"(\d+\.\d{2})$", line)
    price = float(m.group(1)) if m else None
    name = line[:m.start()].strip() if m else line
    return name.upper(), price


def fuzzy(name: str, threshold=88):
    match, score, _ = rapidfuzz.process.extractOne(
        name, CANON, scorer=rapidfuzz.fuzz.ratio
    )
    return (match, score) if score >= threshold else (None, score)
