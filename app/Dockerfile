# app/Dockerfile
FROM python:3.12-slim

# 0. System libs needed by OpenCV, Tesseract and Paddle
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tesseract-ocr libtesseract-dev libleptonica-dev \
    build-essential poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# 1. Prevent pip cache bloat, install deps early
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy source last (layer cache)
COPY . /app

# 3. Expose & non‑root
EXPOSE 8000
RUN useradd -m fastapi
USER fastapi

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
