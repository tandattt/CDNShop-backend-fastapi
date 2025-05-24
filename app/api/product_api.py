from fastapi import APIRouter,Depends
from app.services.product_services import (get_all_product_service,get_all_laptop_by_filter,
                                        get_all_mousePad_by_filter,get_all_mice_by_filter,get_all_headphone_by_filter,
                                        get_deltail_product_service,get_all_screen_by_filter,get_accompanying_products_service)
from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import Optional

router = APIRouter()

@router.get("/get_all")
def get_all_product(name_category: str, db: Session = Depends(get_db)):
    response = get_all_product_service(name_category,db)
    return response

@router.get('/get_accompanying_products')
def get_accompanying_products_api(db: Session = Depends(get_db)):
    # response = get_accompanying_products_repository()
    return get_accompanying_products_service(db)

@router.get("/get_laptop_by_filter")
def get_all_laptop(ram: Optional[str] = None, cpu: Optional[str]= None,
                    screen: Optional[str]= None, storage: Optional[str]= None,
                    brand: Optional[str]= None,min: Optional[int]=0,max: Optional[int]=None, db: Session = Depends(get_db)):
    # Tạo dictionary chứa các tham số
    params = {
        'ram': ram,
        'cpu': cpu,
        'screen': screen,
        'storage': storage,
        'brand': brand,
        'min':min,
        'max':max
    }
    # Lọc bỏ các tham số có giá trị là None
    params = {key: value for key, value in params.items() if value is not None}
    response = get_all_laptop_by_filter(params,db)
    return response

@router.get("/get_mice_by_filter")
def get_all_mouse(color: Optional[str] = None, connectivity_type: Optional[str]= None,
                    dpi: Optional[str]= None, storage: Optional[str]= None,
                    brand: Optional[str]= None,min: Optional[int]=0,max: Optional[int]=None, db: Session = Depends(get_db)):
    # Tạo dictionary chứa các tham số
    params = {
        'color': color,
        'connectivity_type': connectivity_type,
        'dpi': dpi,
        'storage': storage,
        'brand': brand,
        'min':min,
        'max': max
    }
    # Lọc bỏ các tham số có giá trị là None
    params = {key: value for key, value in params.items() if value is not None}
    response = get_all_mice_by_filter(params,db)
    return response



@router.get("/get_headphone_by_filter")
def get_all_headphone(color: Optional[str] = None, connectivity_type: Optional[str]= None,
                    brand: Optional[str]= None,min: Optional[int]=0,max: Optional[int]=None, db: Session = Depends(get_db)):
    # Tạo dictionary chứa các tham số
    params = {
        'color': color,
        'connectivity_type': connectivity_type,
        # 'type': type,
        # 'storage': storage,
        'brand': brand,
        'min':min,
        'max': max
    }
    # Lọc bỏ các tham số có giá trị là None
    params = {key: value for key, value in params.items() if value is not None}
    response = get_all_headphone_by_filter(params,db)
    return response

@router.get("/get_mouse_pab_by_filter")
def get_all_mouse_pab(color: Optional[str] = None, material: Optional[str]= None, size : Optional[str] = None,
                    brand: Optional[str]= None,min: Optional[int]=0,max: Optional[int]=None, db: Session = Depends(get_db)):
    # Tạo dictionary chứa các tham số
    params = {
        'color': color,
        'material': material,
        'size': size,
        # 'storage': storage,
        'brand': brand,
        'min':min,
        'max': max
    }
    # Lọc bỏ các tham số có giá trị là None
    params = {key: value for key, value in params.items() if value is not None}
    response = get_all_mousePad_by_filter(params,db)
    return response

@router.get("/get_screen_by_filter")
def get_all_screen(aspect_ratio: Optional[str] = None, refresh_rate: Optional[str]= None, resolution : Optional[str] = None,
                    screen_size: Optional[str]=None,screen_type: Optional[str]= None, touchscreen: Optional[str]= None,
                    brand: Optional[str]= None,min: Optional[int]=0,max: Optional[int]=None, db: Session = Depends(get_db)):
    # Tạo dictionary chứa các tham số
    params = {
        'aspect_ratio': aspect_ratio,
        'refresh_rate': refresh_rate,
        'resolution': resolution,
        'screen_size': screen_size,
        'screen_type':screen_type,
        'touchscreen':touchscreen,
        'brand': brand,
        'min':min,
        'max': max
    }
    # Lọc bỏ các tham số có giá trị là None
    params = {key: value for key, value in params.items() if value is not None}
    response = get_all_screen_by_filter(params,db)
    return response

@router.get("/get_detail_product")
def get_detail_product_api(product_id: int, db: Session = Depends(get_db)):
    
    response = get_deltail_product_service(product_id,db)
    
    return response