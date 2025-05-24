from fastapi import Response
from fastapi.responses import JSONResponse
from app.repository.user_reposiory import UserRepository
from app.auth.jwt_auth import create_jwt_token
from app.cache.jwt_cache import *
def login_user(username: str,password: str, website: str, db):
    try:
        print(website)
        user_repo = UserRepository(db)
        user = user_repo.check_user(username,password,website)
        
        if user:
            payload = {
                "sub": f"{user.user_id}",
                "name":f"{user.name}"
            }
            print(user.role)
            if user.role == 'admin':
                payload['authorities'] = [
                    "ROLE_ADMIN"
                ]
            else:
                payload['authorities'] = [
                    "ROLE_USER"
                ]
            access_token  = create_jwt_token(payload)
            refresh_token  = create_jwt_token(payload,86000*2)
            set_access_token_cache(access_token,user.user_id)
            set_refresh_token_cache(refresh_token,user.user_id)
            return JSONResponse({
                "message": "Login successful",
                "name":user.name,
                "acces_token":access_token,
                "resfesh_token":refresh_token}, status_code=200)
        return JSONResponse({"message":"username hoặc passwword không đúng"},
            status_code=401
        )
    except Exception as e:
        print(f"Lỗi xảy ra trong check_login: {str(e)}")
        return {"error": "Internal server error", "detail": str(e)}