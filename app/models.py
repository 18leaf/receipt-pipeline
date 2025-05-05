# models.py
from sqlalchemy import Column, Integer, Float, String, DECIMAL, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Receipt(Base):
    __tablename__ = "receipt"
    id = Column(Integer, primary_key=True)
    uploaded_at = Column(TIMESTAMP)
    vendor = Column(String(64))
    total = Column(DECIMAL(8, 2))
    raw_json = Column(JSON)
    items = relationship("Item", back_populates="receipt")


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    receipt_id = Column(Integer, ForeignKey("receipt.id"))
    name = Column(String(64))
    canonical = Column(String(64))
    price = Column(DECIMAL(8, 2))
    confidence = Column(Float)
    receipt = relationship("Receipt", back_populates="items")
