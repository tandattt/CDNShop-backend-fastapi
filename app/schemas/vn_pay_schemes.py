from pydantic import BaseModel
from typing import Optional
class VnPayPaymentRequest(BaseModel):
    order_id: str
    amount: int
    bank_code: Optional[str] = None
    order_desc: str
    locale: str = "vn"
    order_type: str = "other"