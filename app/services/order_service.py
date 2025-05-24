from sqlalchemy.orm import Session
from app.schemas.orders import OrderCreate
from app.repository import order_repository
from app.repository.product_repository import ProductRepository


def create_order_service(db: Session, order_data: OrderCreate):
    return order_repository.create_order(db, order_data)

def get_order_service(db: Session, user_id: int):
    
    data= order_repository.get_order_by_id(db, user_id)
    result = []
    
    for item in data:
        order_item = []
        for i in item.order_items:
            product_repo = ProductRepository(db)
            product = product_repo.get_product_by_id(i.product_id)
            info_product = [{
                "name": product.name,
                "url_img": product.url_img
            }]
            order_item.append({
                "product":info_product,
                "price":i.price,
                "quantity":i.quantity
            })
        result.append({
            "total_amount":item.total_amount,
            "status":item.status,
            "payment_method":item.payment_method,
            "payment_status":item.payment_status,
            "phone":item.phone,
            "order_date":item.order_date,
            "address":item.address,
            "receiving_method":item.receiving_method,
            "name": item.name,
            "order_item": order_item
        })
    
    return result

def update_order_status_service(db: Session, order_id: int, status: str, payment_status: str):
    
    return order_repository.update_order_status(db, order_id, status, payment_status)