import cv2
import numpy as np


def extract_rows(bin_img: np.ndarray) -> list[np.ndarray]:
    # horizontal projection
    hist = cv2.reduce(bin_img, 1, cv2.REDUCE_AVG).reshape(-1)
    h, _ = bin_img.shape
    thresh = 2  # empirical
    is_text = hist > thresh
    rows, start = [], None
    for y, flag in enumerate(is_text):
        if flag and start is None:
            start = y
        elif not flag and start is not None:
            rows.append(bin_img[start:y, :])
            start = None
    if start is not None:
        rows.append(bin_img[start:h, :])
    return rows
