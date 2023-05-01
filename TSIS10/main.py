import psycopg2
from config import host,user,password,db_name

connection = None

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name,
        port= 5433
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )
        
        print(f"Server version: {cursor.fetchone()}")

except Exception as _ex:
    print("[INFO] Error while working with postgresql", _ex)
finally:
    if connection is not None:
        connection.close()
        print("[INFO] Postgresql connection closed")