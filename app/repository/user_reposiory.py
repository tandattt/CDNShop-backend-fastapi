from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate
class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, id: int):
        return self.db.query(User).filter(User.user_id == id).first()
    
    def check_user(self, username: str, password: str, website: str):
        return self.db.query(User).filter(User.username == username, User.password == password, User.role == website).first()
    def create_user(self, user_create: UserCreate):
        db_user = User(**user_create.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user