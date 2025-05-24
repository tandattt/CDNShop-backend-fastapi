from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth_api,cart_api,product_api,view_history_api,gmail_api,vnpay_api,order_api
from app.db.base import Base
from fastapi.openapi.utils import get_openapi


app = FastAPI()


origins = [
    "*"  # nếu frontend deploy lên đây
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # hoặc ["*"] nếu muốn cho tất cả
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_api.router, prefix="/auth", tags=["auth"])
app.include_router(cart_api.router,prefix="/cart",tags=["cart"])
app.include_router(product_api.router,prefix="/product",tags=["product"])
app.include_router(view_history_api.router,prefix="/view",tags=['view_history'])
app.include_router(gmail_api.router, prefix="/gmail",tags=['gmail'])
app.include_router(vnpay_api.router, prefix="/vnpay", tags=["payment"])
app.include_router(order_api.router, prefix="/oder",tags=['oder'])
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="localhost", port=8001, reload=True)