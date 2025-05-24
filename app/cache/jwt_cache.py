from app.core.redis import redis_conn
import json

def get_access_token_cache(access_token: str):
    access = redis_conn.get(f'access:{access_token}')
    if access:
        return access
    None
def set_access_token_cache(access_token: str,user_id: int):
    redis_conn.set(f"access:user{user_id}",access_token,ex=86000)
    
    
def delete_access_token_cache(access_token: str):
    redis_conn.delete(f"access:{access_token}")
    
    
    
def get_refresh_token_cache(user_id: int):
    refresh = redis_conn.get(f'refresh:user{user_id}')
    if refresh:
        return refresh
    None
def set_refresh_token_cache(refresh_token: str,user_id: int):
    redis_conn.set(f"refresh:user{user_id}",refresh_token,ex=86000*2)
    
    
def delete_refresh_token_cache(refresh_token: str):
    redis_conn.delete(f"refresh:{refresh_token}")