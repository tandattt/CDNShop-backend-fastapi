
from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class OrderItem(Base):
    __tablename__ = 'order_items'

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer)
    price = Column(Float)

    order = relationship('Order')
    product = relationship('Product')