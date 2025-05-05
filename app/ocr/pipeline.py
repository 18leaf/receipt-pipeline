import cv2
import io
from .preproc import preprocess
from .line_detect import extract_rows
from .tess import ocr_line
from .postproc import tokenise, fuzzy
import numpy as np


def parse(image_bytes: bytes) -> list[dict]:
    bgr = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    bin_img = preprocess(bgr)
    rows = extract_rows(bin_img)
    items = []
    for r in rows:
        txt = ocr_line(r)
        if not txt:
            continue
        name_raw, price = tokenise(txt)
        if price is None:  # skip headers
            continue
        canonical, score = fuzzy(name_raw)
        items.append(dict(
            raw=name_raw,
            price=price,
            canonical=canonical or name_raw,
            confidence=score
        ))
    return items
