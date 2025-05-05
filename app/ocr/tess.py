import pytesseract
import cv2
import numpy as np
from .config import TESS_ARGS


def ocr_line(img_bin: np.ndarray) -> str:
    # invert for Tesseract
    inv = 255 - img_bin
    text = pytesseract.image_to_string(inv, config=TESS_ARGS)
    return text.strip()
