# models/cart.py
import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from app.db.database import Base

class Cart(Base):
    __tablename__ = "cart"

    cart_id = Column(Integer,primary_key=True,index=True)
    user_id = Column(CHAR(36), ForeignKey("users.user_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, server_default=func.now())

    # Quan hệ nếu muốn:
    user = relationship("User")
    product = relationship("Product")
