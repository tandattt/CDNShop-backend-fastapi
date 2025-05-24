# services/view_history_service.py
from app.repository.view_history_repository import ViewHistoryRepository
from sqlalchemy.orm import Session
from app.models.products import Product
from app.models.mouse_pads import MousePad 

def record_view_history_service(user_id: int, product_id: int, db: Session):
    repo = ViewHistoryRepository(db)
    return repo.add_view(user_id=user_id, product_id=product_id)


def get_nearest_product_by_size(user_id: int, db: Session, limit: int = 5):
    view_repo = ViewHistoryRepository(db)
    last_views = view_repo.get_last_viewed_product(user_id, limit)

    if not last_views:
        return []

    list_product = []
    for view in last_views:
        product = db.query(Product).filter(Product.product_id == view.product_id).first()
        if not product:
            continue
        list_product.append(product)

    result = []
    for product in list_product:
        result.append({
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "category": product.category_id,
            'url_img': product.url_img
        })

    return result

