from app.repository.user_reposiory import UserRepository
from fastapi.responses import JSONResponse
def register_account(body : dict, db):
    try:
        user_repo = UserRepository(db)
        response = user_repo.create_user(body)
        if response:
            return JSONResponse({'message':'successful'},status_code=200)
    except Exception as e:
        # print(f"Lỗi xảy ra trong check_login: {str(e)}")
        return {"error": "Internal server error", "detail": str(e)}
