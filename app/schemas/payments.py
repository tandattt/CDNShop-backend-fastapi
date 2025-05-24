
from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    payment_method: str
    amount: float

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True
