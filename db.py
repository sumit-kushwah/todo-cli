import sqlite3

con = sqlite3.connect('todo.db')

c = con.cursor()

def createTable():
    c.execute("""
        DROP TABLE tasks;
    """)
    c.execute("""CREATE TABLE tasks (
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        recur TEXT,
        project TEXT,
        labels TEXT,
        priority INTEGER,
        completed_date TEXT
    )
    """)
    con.commit()
    con.close()

def createTask(task):
    c.execute("INSERT INTO tasks VALUES(?, ?, ?, ?, ?, ?, ?, ?)", task.to_db_tuple())
    con.commit()
    con.close()

def deleteTask(id):
    res = c.execute(f"""
        DELETE FROM tasks where rowid = {id}
    """).rowcount
    con.commit()
    con.close()
    return res

def getTasks(filters):
    whereclause = ""
    for field, value in filters.items():
        whereclause += f" {field} = '{value}'"
    res = c.execute(f"""
        SELECT rowid, * from tasks where {whereclause}
    """).fetchall()
    con.commit()
    con.close()
    return res

def getTask(id):
    res = c.execute(f"""
        SELECT rowid, * from tasks where rowid = {id}
    """).fetchone()
    con.commit()
    con.close()
    return res
