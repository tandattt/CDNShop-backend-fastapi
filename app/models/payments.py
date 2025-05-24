
from sqlalchemy import Column, Integer, Float, ForeignKey,String
from app.db.database import Base
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    payment_method = Column(String)
    amount = Column(Float)

    order = relationship('Order')
