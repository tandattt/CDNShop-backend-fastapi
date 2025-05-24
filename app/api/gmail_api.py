from fastapi import APIRouter, HTTPException
from app.schemas.email import EmailRequest
from app.utils.gmail_utils import gmail_authenticate, create_message, send_message

router = APIRouter()

@router.post("/send-email")
def send_email_api(email_req: EmailRequest):
    try:
        service = gmail_authenticate()
        message = create_message(email_req.to, email_req.oder_id, email_req.amount)
        message_id = send_message(service, "me", message)
        return {"message": "Email sent", "message_id": message_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
