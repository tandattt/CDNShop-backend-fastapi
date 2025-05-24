from sqlalchemy.orm import Session,joinedload 
from app.models.orders import Order
from app.models.order_items import  OrderItem
from app.schemas.orders import OrderCreate
from typing import Optional

def create_order(db: Session, order_data: OrderCreate):
    order = Order(
        user_id=order_data.user_id,
        status=order_data.status,
        total_amount=order_data.total_amount,
        address=order_data.address,
        payment_method=order_data.payment_method,
        receiving_method=order_data.receiving_method,
        payment_status=order_data.payment_status,
        phone = order_data.phone,
        name = order_data.name
    )

    for item in order_data.order_items:
        order_item = OrderItem(
            product_id=item.product_id,
            price=item.price,
            quantity=item.quantity
        )
        order.order_items.append(order_item)

    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_order_by_id(db: Session, user_id: int):
    return db.query(Order).options(joinedload(Order.order_items)).filter(Order.user_id == user_id).all()

def update_order_status(db: Session, order_id: int, status: Optional[str], payment_status: Optional[str]):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        return None

    if status is not None:
        order.status = status
    if payment_status is not None:
        order.payment_status = payment_status

    db.commit()
    db.refresh(order)
    return order