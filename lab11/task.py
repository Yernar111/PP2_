import psycopg2
from configparser import ConfigParser
def load_config(filename='lab10/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config

config = load_config()
conn = psycopg2.connect(**config)
cur = conn.cursor()

run = True
while run:
    k=str(input("choose and write one of operations -> records/insert/insert_many/query/delete: "))
    if k=="records":
        m=input("choose record -> phone_number/user_name: ")
        cur.callproc('func1',(m,))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
    elif k=="insert":
        m=input("write a phone_number and user_name: ").split()
        cur.execute('call func2(%s, %s)', (int(m[0]), m[1]))
    elif k=="insert_many":
        n=int(input("write a number of rows you want to add: "))
        a=[]
        b=[]
        for i in range(n):
            m=input("write a phone_number and user_name: ").split()
            a.append(int(m[0]))
            b.append(m[1])
        cur.execute('call func3(%s,%s,%s)',(a,b,n))
    elif k=="query":
        m=input("write a column name, then the number of rows that will be selected and skipped respectively: ").split()
        cur.callproc('func4', (m[0],int(m[1]), int(m[2])))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
    elif k=="delete":
        m=input("write a phone_number or user_name: ")
        cur.execute('call func5(%s)', (m,))
    else:
        run = False
    conn.commit()

cur.close()
conn.close()