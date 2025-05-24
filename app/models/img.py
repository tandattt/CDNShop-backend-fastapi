# app/models/img.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Img(Base):
    __tablename__ = "img"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)

    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)

    # Liên kết ngược với bảng Product
    product = relationship("Product")
