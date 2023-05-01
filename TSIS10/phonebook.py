import psycopg2
from psycopg2.extensions import AsIs
from config import host,password,user,db_name




def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        print("PostgreSQL database version: ")
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


def create_tables():
    command = """
    CREATE TABLE users_phones (
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        user_surname VARCHAR(255) NOT NULL,
        phone_number VARCHAR(255) NOT NULL
    )    
    """
    conn = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_data(name, surname, phone_number):
    sql_1 = """
        INSERT INTO users_phones(user_name, user_surname, phone_number)
        VALUES (%s, %s, %s) RETURNING user_id;
    """
    conn = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        cur.execute(sql_1, (name, surname, phone_number))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


def delete_by_name_surname(name, surname):
    conn = None
    sql = """
        DELETE FROM users_phones
        WHERE user_name = (%s) AND user_surname = (%s);
    """
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        cur.execute(sql, (name, surname))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


def import_from_csv(path):
    conn = None
    sql = """
    COPY users_phones
    FROM %s DELIMITER ',' CSV HEADER;
    """
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        cur.execute(sql, (path, ))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


def sort_by_attribute(attribute):
    sql = """
    SELECT * FROM users_phones
    ORDER BY %(attribute)s
    """
    conn = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        cur.execute(sql, {"attribute": AsIs(attribute)})
        for table in cur.fetchall():
            print(table)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


def updated_using_surname(surname):
    option = int(input("Select data to change (1 - name, 2 - phone): "))
    conn = None
    sql_1 = """
    UPDATE users_phones
    set user_name = %s
    WHERE user_surname = %s;
    """
    sql_2 = """
    UPDATE users_phones
    set phone_number = %s
    WHERE user_surname = %s;
    """
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        if option == 1:
            name = input("Enter new name: ")
            cur.execute(sql_1, (name, surname))
        elif option == 2:
            phone_number = input("Enter new phone number: ")
            cur.execute(sql_2, (phone_number, surname))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


