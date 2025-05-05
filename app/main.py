from fastapi import FastAPI, UploadFile, File
from datetime import datetime
import logging

app = FastAPI(title="Receipt‑OCR API", version="0.1.0")


@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok", "ts": datetime.utcnow().isoformat() + "Z"}


@app.post("/upload_receipt", tags=["io"])
async def upload_receipt(file: UploadFile = File(...)):
    # For the first build just echo the payload size.
    payload = await file.read()
    logging.info("Received %s (%d bytes)", file.filename, len(payload))
    return {
        "filename": file.filename,
        "bytes": len(payload),
        "note": "OCR not wired yet; this is only a container smoke test."
    }
