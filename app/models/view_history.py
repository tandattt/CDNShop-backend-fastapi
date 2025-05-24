from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base

class ViewHistory(Base):
    __tablename__ = "view_history"

    view_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    viewed_at = Column(DateTime, default=func.now())
    # device_info = Column(Text)

    user = relationship("User")
    product = relationship("Product")
