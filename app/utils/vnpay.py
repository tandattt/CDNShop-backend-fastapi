import hmac
import hashlib
import urllib.parse
from collections import OrderedDict

class vnpay:
    def __init__(self):
        self.requestData = {}
        self.responseData = {}

    def get_payment_url(self, vnpay_payment_url, secret_key):
        sorted_data = OrderedDict(sorted(self.requestData.items()))

        query_string = "&".join([
            f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sorted_data.items()
        ])

        secure_hash = hmac.new(
            secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha512
        ).hexdigest()

        return f"{vnpay_payment_url}?{query_string}&vnp_SecureHash={secure_hash}"



    def validate_response(self, secret_key):
        input_data = self.responseData.copy()
        vnp_secure_hash = input_data.pop("vnp_SecureHash", None)
        input_data.pop("vnp_SecureHashType", None)

        sorted_data = OrderedDict(sorted(input_data.items()))
        query_string = "&".join([
            f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sorted_data.items()
        ])

        secure_hash = hmac.new(
            secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha512
        ).hexdigest()
        

        secure_hash = hmac.new(
            secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha512
        ).hexdigest()
        print("== VALIDATE DEBUG ==")
        print("Raw data to hash: ", query_string)
        print("Generated hash   : ", secure_hash)
        print("Received hash    : ", vnp_secure_hash)
        return secure_hash == vnp_secure_hash
