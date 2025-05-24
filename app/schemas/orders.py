from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.schemas.order_items import OrderItemCreate

class OrderBase(BaseModel):
    
    status: str
    total_amount: float

    address: Optional[str] = None
    payment_method: Optional[str] = None
    receiving_method: Optional[str] = None
    payment_status: Optional[str] = None

    name: Optional[str] = None     
    phone: Optional[str] = None    


class OrderUpdateStatus(BaseModel):
    status: Optional[str] = None
    payment_status: Optional[str] = None


class OrderCreate(OrderBase):
    user_id: int
    order_items: List[OrderItemCreate]


class Order(OrderBase):
    order_id: int
    user_id: int

    class Config:
        orm_mode = True
