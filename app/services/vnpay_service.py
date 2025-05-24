from datetime import datetime
from app.utils.vnpay import vnpay
from app.core.config import settings


def create_payment_url(data: dict, client_ip: str) -> str:
    vnp = vnpay()
    vnp.requestData["vnp_SecureHashType"] = "SHA512"

    vnp.requestData = {
        "vnp_Version": "2.1.0",
        "vnp_Command": "pay",
        "vnp_TmnCode": settings.VNPAY_TMN_CODE,
        "vnp_Amount": int(data["amount"]) *100,
        "vnp_CurrCode": "VND",
        "vnp_TxnRef": data["order_id"],
        "vnp_OrderInfo": data["order_desc"],
        "vnp_OrderType": data["order_type"],
        "vnp_Locale": data.get("language", "vn"),
        "vnp_CreateDate": datetime.now().strftime('%Y%m%d%H%M%S'),
        "vnp_IpAddr": client_ip,
        "vnp_ReturnUrl": settings.VNPAY_RETURN_URL
    }
    print("1",int(data["amount"]))
    if data.get("bank_code"):
        vnp.requestData["vnp_BankCode"] = data["bank_code"]

    return vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)


def validate_vnpay_response(params: dict) -> dict:
    vnp = vnpay()
    vnp.responseData = params
    
    if not vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
        # print("1")
        return {"status": "invalid", "message": "Dữ liệu không hợp lệ"}
    # print("1")
    response_code = params.get("vnp_ResponseCode")
    if response_code == "00":
        print("2",int(params.get("vnp_Amount", 0)) // 100)
        return {
            "status": "success",
            "message": "Thanh toán thành công",
            "order_id": params.get("vnp_TxnRef"),
            "amount": int(params.get("vnp_Amount", 0)) // 100,
            "transaction_no": params.get("vnp_TransactionNo"),
            "pay_date": params.get("vnp_PayDate")
        }
    else:
        return {
            "status": "fail",
            "message": "Thanh toán thất bại",
            "response_code": response_code
        }
