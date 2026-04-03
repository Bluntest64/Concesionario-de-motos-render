import psycopg2
import os
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URL"),
        cursor_factory=RealDictCursor)