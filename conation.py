import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
pasw = os.getenv("PASSWORD_DB")
def contion_db():
    try: 
        conn = psycopg2.connect(
        port = 5432,
        host = "localhost",                       
        user = "postgres",
        database = "ps_db",
        password = pasw
    )
    except Exception as error:
        print(f"Conation error:{error}")

    return conn
    
def create_tabele():
    conn = contion_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks( 
                task_id serial primary key,
                title varchar(30) NOT NULL,
                description text,
                duration date NOT NULL,
                status boolean DEFAULT false,
                created_at timestamp DEFAULT NOW(),
                is_active boolean DEFAULT true
                ); 
            """)
        conn.commit()
        cur.close()
        print("Table created!")
    except Exception as error:
        print(f"Erro in create tabele: {error}")
        
        
        



