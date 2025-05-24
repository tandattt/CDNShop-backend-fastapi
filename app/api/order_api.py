from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.orders import OrderCreate, Order, OrderUpdateStatus
from app.db.database import get_db
from app.services.order_service import create_order_service, get_order_service, update_order_status_service

router = APIRouter()

@router.post("/create")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    return create_order_service(db, order_data)


@router.get("/get_by_id")
def get_order(user_id: int, db: Session = Depends(get_db)):
    order = get_order_service(db, user_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}")
def update_order_status(order_id: int, update_data: OrderUpdateStatus, db: Session = Depends(get_db)):
    updated_order = update_order_status_service(
        db,
        order_id,
        status=update_data.status,
        payment_status=update_data.payment_status
    )
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return ({"message":"sucess"})

# @router.get("/get_oder")