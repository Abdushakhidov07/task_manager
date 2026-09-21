from conation import contion_db



def get_task(task_id):
    conn = contion_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            select * from tasks where  task_id = %s
            """, (task_id,))
        data = cur.fetchall()
        for task in data:
            print(f"""
        Your Task      
Task id:{task[0]}
Task titile:{task[1]}
Task description:{task[2]}
Task duration:{task[3]}
Task status:{task[4]}
                  """)

    except Exception as error:
        print(f"Erro in get data task: {error}")
    finally: 
        conn.commit()
        cur.close()
        conn.close()
        
        

def create_task(title, descrp, duration):
    conn = contion_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO tasks(title, description, duration) VALUES
            (%s, %s, %s)
            """, (title, descrp, duration,))
    except Exception as error:
        print(f"Erro in add data task: {error}")
    finally: 
        conn.commit()
        cur.close()
        conn.close()
        

