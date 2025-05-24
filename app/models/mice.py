
from sqlalchemy import Column, Integer, String, ForeignKey,Float
from app.db.database import Base
from sqlalchemy.orm import relationship
class Mouse(Base):
    __tablename__ = 'mice'
    mice_id=Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    # type = Column(String)
    connectivity_type = Column(String)
    dpi = Column(Integer)
    color = Column(String)

    product = relationship('Product')
