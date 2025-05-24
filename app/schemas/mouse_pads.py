
from pydantic import BaseModel

class MousePadBase(BaseModel):
    material: str
    size: str
    color: str

class MousePadCreate(MousePadBase):
    pass

class MousePad(MousePadBase):
    product_id: int

    class Config:
        orm_mode = True
