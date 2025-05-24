from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    to: EmailStr
    oder_id: str
    amount: float
    