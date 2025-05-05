import pytesseract

TESS_CMD = "/usr/bin/tesseract"
pytesseract.pytesseract.tesseract_cmd = TESS_CMD

TESS_ARGS = r"--oem 3 --psm 6 -c preserve_interword_spaces=1"
LEXICON_PATH = "/app/lexicon.txt"
