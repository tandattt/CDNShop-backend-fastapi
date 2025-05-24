from dotenv import load_dotenv
import os
load_dotenv()
class Settings:
    DATABASE_URL : str = os.getenv('DATABASE_URL')
    
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: int = os.getenv("REDIS_PORT")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD")
    REDIS_DB: int = os.getenv("REDIS_DB")
    
    JWT_SECRET_KEY : str = os.getenv("JWT_SECRET_KEY")
    
    SCOPES: str = os.getenv("SCOPES")
    TOKEN_PICKLE:str = os.getenv("TOKEN_PICKLE")
    CLIENT_SECRET_FILE: str = os.getenv("CLIENT_SECRET_FILE")
    
    VNPAY_TMN_CODE = os.getenv("VNPAY_TMN_CODE")
    VNPAY_HASH_SECRET_KEY = os.getenv("VNPAY_HASH_SECRET_KEY")
    VNPAY_PAYMENT_URL = os.getenv("VNPAY_PAYMENT_URL")
    VNPAY_RETURN_URL = os.getenv("VNPAY_RETURN_URL")

settings = Settings()

