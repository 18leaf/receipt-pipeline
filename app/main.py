# main.py (replace stub)
from datetime import datetime
from fastapi import BackgroundTasks, FastAPI, UploadFile, File
from ocr.pipeline import parse
from models import Base, Receipt, Item
from sqlalchemy.orm import Session
import logging
import json
from sqlalchemy import create_engine, text
import os

log = logging.getLogger("api")
log.setLevel(logging.INFO)

engine = create_engine(os.getenv("DB_URI"))

app = FastAPI(title="Receipt‑OCR API", version="0.1.0")


def save_receipt_stub():
    # create an empty receipt record, return id
    with engine.begin() as conn:
        rid = conn.execute(
            text("INSERT INTO receipt (vendor,total,raw_json) VALUES ('UNKNOWN',0,'{}')"))
        return rid.lastrowid


@app.post("/upload_receipt")
async def upload(file: UploadFile = File(...)):
    payload = await file.read()
    items = parse(payload)
    log.info("parsed %d items", len(items))

    total = round(sum(i["price"] for i in items if i["price"]), 2)

    with Session(engine) as s:
        r = Receipt(vendor="UNKNOWN", total=total, raw_json=json.dumps(items))
        s.add(r)
        s.flush()
        rid = r.id
        s.bulk_save_objects([
            Item(receipt_id=rid, name=i["raw"],
                 canonical=i["canonical"], price=i["price"],
                 confidence=i["confidence"])
            for i in items
        ])
        s.commit()
    return {"id": rid, "item_count": len(items), "total": total}


@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok", "ts": datetime.utcnow().isoformat() + "Z"}
