from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, DECIMAL
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime
class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(255))
    total_amount = Column(DECIMAL(15, 2))

    user_id = Column(Integer, ForeignKey('users.user_id'))
    address = Column(String(255))
    payment_method = Column(String(50))
    receiving_method = Column(String(50))
    payment_status = Column(String(50))

    name = Column(String(255))
    phone = Column(String(20))  

    user = relationship("User")
    order_items = relationship("OrderItem", cascade="all, delete")
