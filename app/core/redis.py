import redis
from redis.connection import SSLConnection
from app.core.config import settings

pool = redis.ConnectionPool(
    connection_class=SSLConnection,
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD,
    decode_responses=True
)

redis_conn = redis.Redis(connection_pool=pool)
