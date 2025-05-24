from app.repository.product_repository import ProductRepository
from sqlalchemy.orm import Session


def get_all_product_service(name_category : str, db: Session):
    product_repo = ProductRepository(db)
    products = product_repo.get_product_repository(name_category)
    if not products:
        return "ứ có nha bờ rô"

    result = []
    for product in products:
        product_dict = {
            "product_id": product.product_id,
            "name": product.name,
            # "description": product.description,
            "price": product.price,
            # "stock_quantity": product.stock_quantity,
            "category": product.category.name if product.category else None,
            "url_img": product.url_img
            # "imgs": [img.url for img in product.imgs]  # chỉ lấy URL ảnh
        }
        result.append(product_dict)
        config_product = product_repo.get_config_product(product.product_id,product.category.name)
        for field in ["laptop_id", "product_id", "brand_id","headphone_id","screen_id","mice_id","mouse_pad_id"]:
            if hasattr(config_product, field):
                delattr(config_product, field)

        product_dict.update({"config_product":config_product})
    return result

def get_accompanying_products_service(db: Session):
    return ProductRepository(db).get_accompanying_products_repository()

def get_all_laptop_by_filter(params: dict,db:Session):
    laptop_repo = ProductRepository(db)
    response = laptop_repo.get_laptop_repository(params)
    return response

def get_all_mice_by_filter(params: dict,db:Session):
    mice_repo = ProductRepository(db)
    response = mice_repo.get_mice_repository(params)
    return response
    
def get_all_headphone_by_filter(params: dict,db:Session):
    headphone_repo = ProductRepository(db)
    response = headphone_repo.get_headphone_repository(params)
    
    return response
    
def get_all_mousePad_by_filter(params: dict,db:Session):
    mouse_pab_repo = ProductRepository(db)
    response = mouse_pab_repo.get_mouse_pad_repository(params)
    
    return response

def get_all_screen_by_filter(params: dict,db:Session):
    screen_repo = ProductRepository(db)
    response = screen_repo.get_screen_repository(params)
    
    return response

def get_deltail_product_service(product_id: int, db: Session):
    pro_repo = ProductRepository(db)
    product = pro_repo.get_detail_product_repo(product_id)
    if not product:
        return "ứ có nha bờ rô"


    product_dict = {
        "product_id": product.product_id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        # "stock_quantity": product.stock_quantity,
        # "category": product.category.name if product.category else None,
        "url_img": product.url_img,
        "brand": product.brand.name,
        "imgs": [img.url for img in product.imgs]  # chỉ lấy URL ảnh
    }
    # print(product_id,product.category.name)
    config_product = pro_repo.get_config_product(product_id,product.category.name)
    for field in ["laptop_id", "product_id", "brand_id","headphone_id","screen_id","mice_id","mouse_pad_id"]:
        if hasattr(config_product, field):
            delattr(config_product, field)

    product_dict.update({"config_product":config_product})
    # result.append(product_dict)

    return product_dict