
from pydantic import BaseModel
from typing import List, Text

class ProductBase(BaseModel):
    name: str
    description: Text
    price: float
    stock_quantity: int

class ProductCreate(ProductBase):
    category_id: int
    brand_id: int

class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
