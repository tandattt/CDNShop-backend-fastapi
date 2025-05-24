# schemas/cart.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CartBase(BaseModel):
    user_id: str
    product_id: int
    quantity: int = 1

class CartItem(BaseModel):
    product_id: int
    quantity: int = 1

class CartCreate(BaseModel):
    user_id: str
    cart: list[CartItem]
    
class CartResponse(CartBase):
    cart_id: str
    created_at: datetime
    
    class Config:
        orm_mode = True
