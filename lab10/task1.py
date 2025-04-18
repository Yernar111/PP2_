import psycopg2
import csv
from configparser import ConfigParser
def load_config(filename='lab10/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config 

def insert2(file):
    with open(file, "r") as file:
        read = csv.reader(file)
        for row in read:
            cur.execute(insert, (row[0], row[1]))

def select(m):
    cur.execute(f"SELECT {m} from phone_book1")
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()


config = load_config()
conn = psycopg2.connect(**config)
cur = conn.cursor()

insert = "INSERT INTO phone_book1(phone_number, user_name) VALUES(%s, %s);"
update1 = "UPDATE phone_book1 set phone_number = %s where phone_number = %s;"
update2 = "UPDATE phone_book1 set user_name = %s where user_name = %s;"
delete = "DELETE FROM phone_book1 where user_name = %s;"

cur.execute("create table if not exists phone_book1(phone_number int PRIMARY KEY, user_name varchar(20));")

run = True
while run:
    k=str(input("choose and write one of operations -> insert/update/select/delete: "))
    if k=="insert":
        m=int(input("1: insert from console. 2: insert from csv file "))
        if m==2:
            m=input("Write the file name: ")
            insert2(m)
        elif m==1:
            m=input("write phone number and user name: ").split()
            cur.execute(insert, (m[0], m[1]))
    elif k=="update":
        t=input("choose the column that has a cell which will change: ")
        m=input("choose the name of cell you want to change, then a new value: ").split()
        if t=="phone_number":
            cur.execute(update1, (m[1], m[0]))
        elif t=="user_name":
            cur.execute(update2, (m[1], m[0]))
    elif k=="select":
        m=input("choose the column you want to select or write * if you want to select all of them: ")
        select(m)
    elif k=="delete":
        m=input("add the name of user you want to delete from table: ")
        cur.execute(delete,(m,))
    elif k=="quit":
        run = False
    conn.commit()

cur.close()
conn.close()