import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from app.core.config import settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from fastapi import Depends, HTTPException

security = HTTPBearer()
SECRET_KEY = settings.JWT_SECRET_KEY

def create_jwt_token(payload: dict, expires_in_seconds: int = 86000):
    payload_copy = payload.copy()
    print(expires_in_seconds)
    payload_copy["exp"] = datetime.utcnow() + timedelta(seconds=expires_in_seconds)
    payload_copy["iat"] = datetime.utcnow()
    token = jwt.encode(payload_copy, SECRET_KEY, algorithm="HS256")
    return token

def decode_jwt_token(token: str):
    print(token)
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        # Kiểm tra thời gian hết hạn thủ công (1 ngày tính từ thời điểm phát hành)
        if "exp" in decoded:
            exp_time = datetime.fromtimestamp(decoded["exp"])
            now = datetime.utcnow()

            if now > exp_time:
                return {"valid": False, "error": "Token quá hạn cho phép"}
            
            # if (exp_time - now) > timedelta(seconds=1):
            #     return {"valid": True, "payload": decoded}
                
            return {"valid": True, "payload": decoded}
        

    except ExpiredSignatureError as e:
        return {"valid": False, "error": str(e)}
    except InvalidTokenError:
        return {"valid": False, "error": "Token không hợp lệ"}
def veriry_token(auth_header):
    if not auth_header or not auth_header.startswith('Bearer '):
        return {"valid": False, "error": "Thiếu hoặc sai định dạng Authorization header"}

    token = auth_header.split('Bearer ')[1]
    result = decode_jwt_token(token)
    return result  # Luôn là dict {valid, error?, payload?}

