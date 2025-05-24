from fastapi import APIRouter,Depends
from app.schemas.cart import CartCreate, CartItem
from app.services.cart_services import create_cart_service,update_cart_service,get_detail_cart_service,delete_cart_service,get_total_cart_service
from sqlalchemy.orm import Session
from app.db.database import get_db
router = APIRouter()

@router.post("/add_cart")
def create_cart_api(body: CartCreate, db: Session = Depends(get_db)):
    response = create_cart_service(body,db)
    return response

@router.patch("/update_cart/{user_id}")
def update_cart_api(user_id: int,body: CartItem,db: Session = Depends(get_db)):
    product_id = body.product_id
    quantity = body.quantity
    response = update_cart_service(user_id,product_id,quantity,db)
    return response

@router.get("/detail_cart")
def get_detail_cart_api(user_id: int, db: Session = Depends(get_db)):
    response = get_detail_cart_service(user_id,db)
    return response

@router.delete('/delete_cart')
def delete_cart_api(user_id: int,product_id: int, db: Session = Depends(get_db)):
    return delete_cart_service(user_id,product_id,db)

@router.get("/get_total_cart")
def get_total_cart(user_id: int, db: Session = Depends(get_db)):
    return ({"total_cart":get_total_cart_service(user_id,db)})
    