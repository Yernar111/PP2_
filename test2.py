import psycopg2
from config import load_config
def create_tables():
    commands = """ CREATE TABLE phone_book (phone_number SERIAL PRIMARY KEY, user_name VARCHAR(255); """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(commands)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_vendor(user_name, phone_number):
    sql = """INSERT INTO phone_book ("phone_number", "user_name")
             VALUES(%s, %s);"""
    vendor_id = None
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (user_name,phone_number))
                # get the generated id back
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
user_name=input()
phone_number=input()
if __name__ == '__main__':
    create_tables()
    insert_vendor(user_name, phone_number)


