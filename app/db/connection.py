import psycopg2
from psycopg2.extras import RealDictCursor
from core.config import settings


def get_connection():
    conn = psycopg2.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        cursor_factory=RealDictCursor
    )
    return conn
