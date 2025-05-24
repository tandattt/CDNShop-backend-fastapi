
from pydantic import BaseModel
from typing import Optional

class OrderItemBase(BaseModel):
    # order_id: int
    product_id: int
    quantity: int
    price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True
