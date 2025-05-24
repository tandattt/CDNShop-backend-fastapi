from app.services.login_services import login_user
from app.services.register_services import register_account
from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.users import UserLogin,UserCreate
from app.db.database import get_db
router = APIRouter()


@router.post("/login")
def login_api( body: UserLogin, db : Session = Depends(get_db)):
    username = body.username
    password = body.password
    website = body.website
    return login_user(username,password,website, db)
@router.post("/register")
def register_api(body : UserCreate, db : Session = Depends(get_db)):
    return register_account(body,db)

