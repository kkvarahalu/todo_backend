import mysql.connector

def get_db_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pallavi",
        database="todo_db"
    )
    return conn

def init_db():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('''create table if not exists tasks(
    id int auto_increment primary key,
    title varchar(255) not null,
    description text,
    completed boolean default false 
    )
    ''')
    conn.commit()
    conn.close()
init_db()
