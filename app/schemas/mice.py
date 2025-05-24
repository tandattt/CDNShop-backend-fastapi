
from pydantic import BaseModel

class MouseBase(BaseModel):
    type: str
    connectivity_type: str
    dpi: int
    color: str

class MouseCreate(MouseBase):
    pass

class Mouse(MouseBase):
    product_id: int
    brand_id: int

    class Config:
        orm_mode = True
