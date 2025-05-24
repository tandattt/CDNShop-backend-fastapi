
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.view_history_service import record_view_history_service,get_nearest_product_by_size

router = APIRouter()

@router.post("/record")
def record_view(user_id: int, product_id: int, db: Session = Depends(get_db)):
    #  request: Request,
    # user_agent = request.headers.get("User-Agent", "unknown")
    view = record_view_history_service(user_id, product_id, db)
    return {"message": "View recorded", "view_id": str(view.view_id)}

@router.get("/history")
def recommend_by_last_size(user_id: int, db: Session = Depends(get_db)):
    data = get_nearest_product_by_size(user_id, db)
    return data