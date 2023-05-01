import psycopg2
from config import host,password,db_name,user



def connect():
    conn = None
    try:
        
        print("Connecting to database...")
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
    command_1 = """
    CREATE TABLE users_score (
        user_id INTEGER PRIMARY KEY,
        score INTEGER NOT NULL,
        level INTEGER NOT NULL,
        speed INTEGER NOT NULL,
        FOREIGN KEY (user_id)
        REFERENCES users (user_id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    """
    command_2 = """
        CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        user_name CHARACTER VARYING(30)
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
        cur.execute(command_2)
        cur.execute(command_1)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
       conn.close()


def is_username_exist(username):
    sql = """
    SELECT * FROM users WHERE user_name = %s
    """
    conn = None
    is_exist = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        cur.execute(sql, (username, ))
        is_exist = cur.fetchone()[0]
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return is_exist


def get_id(username):
    sql = """
    SELECT user_id FROM users WHERE user_name = %s;
    """
    conn = None
    id = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port= 5433
            )
        cur = conn.cursor()
        cur.execute(sql, (username, ))
        id = cur.fetchone()[0]
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return id


def get_scores_by_id(id):
    sql = """
    SELECT * FROM users_score WHERE user_id = %s
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
        cur.execute(sql, (id, ))
        data = cur.fetchone()
        for line in data:
            print(line)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def insert_scores(user_id, score, level, speed):
    conn = None
    sql = """
    INSERT INTO users_score (user_id, score, level, speed)
    VALUES (%s, %s, %s, %s);
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
        cur.execute(sql, (user_id, score, level, speed))
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def insert_username(username):
    sql = """
    INSERT INTO users (user_name)
    VALUES (%s) RETURNING user_id;
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
        cur.execute(sql, (username,))
        data = cur.fetchone()
        for line in data:
            print(line)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


create_tables()