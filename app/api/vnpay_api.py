from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse,RedirectResponse
from app.services.vnpay_service import create_payment_url, validate_vnpay_response
from app.schemas.vn_pay_schemes import VnPayPaymentRequest
from typing import Optional
from app.utils.gmail_utils import  gmail_authenticate, create_message, send_message
from urllib.parse import parse_qs,unquote_plus
router = APIRouter()

@router.post("/payment")
async def payment(request: Request, body: VnPayPaymentRequest):
    try:
        x_forwarded = request.headers.get("x-forwarded-for")
        client_ip = x_forwarded or request.client.host

        url = create_payment_url(body.dict(), client_ip)
        return {"payment_url": url}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/payment-return")
async def payment_return(
    raw_query: Optional[str] = Query(
        None,
        title="VNPAY Query String",
        description="Dán nguyên chuỗi query VNPAY (vd: vnp_TxnRef=...&vnp_Amount=...)"
    ),
    request: Request = None
):
    
    if raw_query:
        # Decode 2 lớp
        raw_query = unquote_plus(unquote_plus(raw_query))  # hoặc dùng: unquote(unquote(raw_query))
        query_dict = {k: v[0] for k, v in parse_qs(raw_query).items()}
    else:
        query_dict = dict(request.query_params)

    result = validate_vnpay_response(query_dict)
    if result["status"] == "invalid":
        raise HTTPException(status_code=400, detail=result["message"])

    return JSONResponse(content=result)




@router.get("/return")
async def vnpay_return(request: Request):
    params = dict(request.query_params)

    vnp_response_code = params.get("vnp_ResponseCode")
    order_id = params.get("vnp_TxnRef")
    amount = int(params.get("vnp_Amount", 0)) // 100
    email = params.get("vnp_OrderInfo")  
    print(amount)
    if vnp_response_code == "00" and email:
        try:
            service = gmail_authenticate()
            message = create_message(email, order_id, amount)
            send_message(service, "me", message)
        except Exception as e:
            print("Lỗi gửi email:", e)

    redirect_url = f"http://localhost:5173/cart?vnp_ResponseCode={vnp_response_code}&orderId={order_id}"
    return RedirectResponse(url=redirect_url)
