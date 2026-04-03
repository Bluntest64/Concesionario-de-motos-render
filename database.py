import psycopg2
import os

def get_connection():
    return psycopg2.connect(os.environ.get("postgresql://usuario:tDDjysXCnrQD3dT9FkvQU3vogISl9pLb@dpg-d76u8via214c73d5o4ig-a.oregon-postgres.render.com/database_5rjq"))