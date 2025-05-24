from app.schemas.cart import CartCreate
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.repository.cart_repository import CartRepository
from app.repository.product_repository import ProductRepository

def create_cart_service(body: CartCreate, db: Session):
    cart_repo = CartRepository(db)

    try:
        for item in body.cart:
            existing_cart = cart_repo.get_cart_by_user_product(body.user_id, item.product_id)

            if existing_cart:
                existing_cart.quantity += item.quantity
                db.commit()
            else:
                new_cart = cart_repo.create_cart(
                    user_id=body.user_id,
                    product_id=item.product_id,
                    quantity=item.quantity
                )
        get_total_cart = cart_repo.get_all_by_userId(body.user_id)
        total_cart = sum(item.quantity for item in get_total_cart)
        
        return {"total_cart": total_cart}
    
    except Exception as e:
        db.rollback()
        return {
            "status": "error",
            "message": f"Error while updating cart: {str(e)}"
        }

def update_cart_service(user_id :int, product_id:int, quantity:int,db: Session):
    cart_repo = CartRepository(db)
    
    cart = cart_repo.get_cart_by_user_product(user_id,product_id)
    
    if not cart:
        return "loi"
    cart.quantity = quantity
    db.commit()
    
    return{"mesage":"success"}

def get_detail_cart_service(user_id: int, db: Session):
    cart_repo = CartRepository(db)
    
    cart = cart_repo.get_all_by_userId(user_id)
    product_repo = ProductRepository(db)
    list_cart = []
    response = []
    total_price = 0
    for item in cart:
        info_product = product_repo.get_product_by_id(item.product_id)
        list_cart.append({
            "name_prodcut":info_product.name,
            "price":info_product.price,
            "quantity":item.quantity,
            "url_img": info_product.url_img,
            "product_id":info_product.product_id
        })
        total_price += info_product.price
    response.append({
        "total_price":total_price,
        "cart":list_cart
    })
    return response

def delete_cart_service(user_id: int, product_id: int, db: Session):
    cart_repo = CartRepository(db)
    
    product = cart_repo.get_cart_by_user_product(user_id,product_id)
    if product:
        try:
            db.delete(product)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        return ({"message":"xóa thành công"})
    
def get_total_cart_service(user_id: int, db: Session):
    cart_repo = CartRepository(db)
    
    total_cart = 0
    cart = cart_repo.get_all_by_userId(user_id)
    for item in cart:
        total_cart += item.quantity
    return total_cart