from sqlalchemy.orm import Session, joinedload
from app.models.products import Product
from app.models.categories import Category
from app.models.img import Img
from app.models.laptops import Laptop
from app.models.mice import Mouse
from app.models.headphones import Headphone
from app.models.brands import Brand
from app.models.mouse_pads import MousePad
from app.models.screens import Screen
from sqlalchemy.sql import func


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
    
    model_map = {
        "Laptop": Laptop,
        "Mice": Mouse,
        "HeadPhone": Headphone,
        "MousePad": MousePad,
        "Screen": Screen
    }    
    
    def get_product_by_id(self,product_id: int):
        return (self.db.query(Product).filter(Product.product_id == product_id).first())
    
    def get_product_repository(self,name_caterogy: str):
        # print (name_caterogy)
        return (self.db.query(Product)
                .join(Product.category)
                .filter(Category.name == name_caterogy).all())
        
    def get_config_product(self,product_id:int, category_name: str):
        model_cls = self.model_map.get(category_name)
        print(category_name)
        if not model_cls:
            raise ValueError("Unsupported category")

        query = self.db.query(model_cls).filter(model_cls.product_id == product_id)
        return query.first()
    
    def get_detail_product_repo(self, product_id: int):
        return (self.db.query(Product)
                .options(
                    joinedload(Product.category),
                    joinedload(Product.imgs),
                    joinedload(Product.brand)
                )
                .filter(Product.product_id == product_id).first())
    def get_accompanying_products_repository(self):
        result = []
        query_mouse = self.db.query(Mouse).join(Mouse.product).options(joinedload(Mouse.product)).order_by(func.rand()).first()
        if query_mouse:
            result.append({
                "name":query_mouse.product.name,
                "url_img": query_mouse.product.url_img,
                "product_id": query_mouse.product_id,
                "mouse_id":query_mouse.mice_id,
                "price": query_mouse.product.price
                
            })
        query_headphone =self.db.query(Headphone).join(Headphone.product).options(joinedload(Headphone.product)).order_by(func.rand()).first()
        if query_headphone:
            result.append({
                "name":query_headphone.product.name,
                "url_img": query_headphone.product.url_img,
                "product_id": query_headphone.product_id,
                "headphone_id": query_headphone.headphone_id,
                "price": query_headphone.product.price
                
            })
        query_mouse_pab = self.db.query(MousePad).join(MousePad.product).options(joinedload(MousePad.product)).order_by(func.rand()).first()
        if query_mouse_pab:
            result.append({
                "name":query_mouse_pab.product.name,
                "url_img": query_mouse_pab.product.url_img,
                "product_id": query_mouse_pab.product_id,
                "mouse_pab_id":query_mouse_pab.mouse_pad_id,
                "price": query_mouse_pab.product.price
                
            })
        return result
        
    def get_laptop_repository(self, filters: dict):
        query = (
            self.db.query(Laptop)
            .join(Laptop.product)
            .join(Product.brand)
            .options(joinedload(Laptop.product).joinedload(Product.brand))
        )

        if 'brand' in filters:
            query = query.filter(Brand.name == filters['brand'])

        for key, value in filters.items():
            if key in ['brand', 'min', 'max']:
                continue
            column = getattr(Laptop, key, None)
            if column and value:
                query = query.filter(column == value)

        min_price = filters.get("min", 0)
        max_price = filters.get("max")

        result = []
        for laptop in query:
            product = laptop.product
            if not product:
                continue

            price = product.price
            if (max_price is not None and min_price < price <= max_price) or (max_price is None and price > min_price):
                result.append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": price,
                    "url_img": product.url_img,
                    "config_product": {
                        "cpu": laptop.cpu,
                        "ram": laptop.ram,
                        "storage": laptop.storage,
                        "screen": laptop.screen,
                    }
                })

        return result

    def get_mice_repository(self, filters: dict):
        query = (
            self.db.query(Mouse)
            .join(Mouse.product)
            .join(Product.brand)
            .options(joinedload(Mouse.product).joinedload(Product.brand))
        )

        if 'brand' in filters:
            query = query.filter(Brand.name == filters['brand'])

        for key, value in filters.items():
            if key in ['brand', 'min', 'max']:
                continue
            column = getattr(Mouse, key, None)
            if column and value:
                query = query.filter(column == value)

        min_price = filters.get("min", 0)
        max_price = filters.get("max")

        result = []
        for mouse in query:
            product = mouse.product
            if not product:
                continue

            price = product.price
            if (max_price is not None and min_price < price <= max_price) or (max_price is None and price > min_price):
                result.append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": price,
                    "url_img": product.url_img,
                    "config_product": {
                        "dpi": mouse.dpi,
                        "connectivity_type": mouse.connectivity_type,
                        "color": mouse.color
                    }
                })

        return result

    
    def get_headphone_repository(self, filters: dict):
        query = (
            self.db.query(Headphone)
            .join(Headphone.product)
            .join(Product.brand)
            .options(joinedload(Headphone.product).joinedload(Product.brand))
        )

        if 'brand' in filters:
            query = query.filter(Brand.name == filters['brand'])

        for key, value in filters.items():
            if key in ['brand', 'min', 'max']:
                continue
            column = getattr(Headphone, key, None)
            if column and value:
                query = query.filter(column == value)

        min_price = filters.get("min", 0)
        max_price = filters.get("max")

        result = []
        for headphone in query:
            product = headphone.product
            if not product:
                continue

            price = product.price
            if (max_price is not None and min_price < price <= max_price) or (max_price is None and price > min_price):
                result.append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": price,
                    "url_img": product.url_img,
                    "config_product": {
                        "color": headphone.color,
                        "connectivity_type": headphone.connectivity_type,
                        "battery_life": headphone.battery_life
                    }
                })

        return result


    def get_mouse_pad_repository(self, filters: dict):
        query = (
            self.db.query(MousePad)
            .join(MousePad.product)
            .join(Product.brand)
            .options(joinedload(MousePad.product).joinedload(Product.brand))
        )

        if 'brand' in filters:
            query = query.filter(Brand.name == filters['brand'])

        for key, value in filters.items():
            if key in ['brand', 'min', 'max']:
                continue
            column = getattr(MousePad, key, None)
            if column and value:
                query = query.filter(column == value)

        min_price = filters.get("min", 0)
        max_price = filters.get("max")

        result = []
        for mouse_pad in query:
            product = mouse_pad.product
            if not product:
                continue

            price = product.price
            if (max_price is not None and min_price < price <= max_price) or (max_price is None and price > min_price):
                result.append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": price,
                    "url_img": product.url_img,
                    "config_product": {
                        "material": mouse_pad.material,
                        "size": mouse_pad.size,
                        "color": mouse_pad.color
                    }
                })

        return result




    def get_screen_repository(self, filters: dict):
        query = (
            self.db.query(Screen)
            .join(Screen.product)
            .join(Product.brand)
            .options(joinedload(Screen.product).joinedload(Product.brand))
        )

        if 'brand' in filters:
            query = query.filter(Brand.name == filters['brand'])

        for key, value in filters.items():
            if key in ['brand', 'min', 'max']:
                continue
            column = getattr(Screen, key, None)
            if column and value:
                query = query.filter(column == value)

        result = []
        for screen in query:
            product = screen.product
            if not product:
                continue

            price = product.price
            min_price = filters.get("min", 0)
            max_price = filters.get("max")

            if max_price is not None:
                if min_price < price <= max_price:
                    result.append({
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": price,
                        "url_img": product.url_img,
                        "config_product": {
                            "screen_size": screen.screen_size,
                            "screen_type": screen.screen_type,
                            "refresh_rate": screen.refresh_rate,
                            "touchscreen": screen.touchscreen,
                            "resolution": screen.resolution,
                            "aspect_ratio": screen.aspect_ratio
                        }
                    })
            else:
                if price >= min_price:
                    result.append({
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": price,
                        "url_img": product.url_img,
                        "config_product": {
                            "screen_size": screen.screen_size,
                            "screen_type": screen.screen_type,
                            "refresh_rate": screen.refresh_rate,
                            "touchscreen": screen.touchscreen,
                            "resolution": screen.resolution,
                            "aspect_ratio": screen.aspect_ratio
                        }
                    })

        return result

