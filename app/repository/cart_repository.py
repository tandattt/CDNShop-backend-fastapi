from sqlalchemy.orm import Session
from app.schemas.cart import CartCreate
from app.models.cart import Cart

class CartRepository:
    def __init__(self,db : Session):
        self.db = db
    def create_cart(self, user_id: str, product_id: int, quantity: int = 1):
        new_cart = Cart(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )
        self.db.add(new_cart)
        self.db.commit()
        self.db.refresh(new_cart)
        return new_cart
    def get_cart_by_user_product(self, user_id: int, product_id: int):
        return self.db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).first()
    def get_all_by_userId(self, user_id: int):
        return self.db.query(Cart).filter(Cart.user_id == user_id).all()