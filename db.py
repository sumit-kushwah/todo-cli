import sqlite3

con = sqlite3.connect('todo.db')

from prettytable import from_db_cursor

c = con.cursor()

def createTable():
    c.execute("""
        DROP TABLE tasks;
    """)
    c.execute("""CREATE TABLE tasks (
        title TEXT NOT NULL,
        note TEXT,
        date TEXT,
        recur TEXT,
        project TEXT,
        is_completed BOOL
    )
    """)
    con.commit()
    con.close()

def createTask(task):
    c.execute("INSERT INTO tasks VALUES(?, ?, ?, ?, ?, ?)", task.to_db_tuple())
    con.commit()
    con.close()

def deleteTask(id):
    res = c.execute(f"""
        DELETE FROM tasks where rowid = {id}
    """).rowcount
    con.commit()
    con.close()
    return res

def getTasks(filters, skipFilter=False):
    if skipFilter:
        query = "SELECT * from tasks"
    else:
        filters['project']
        whereclause = f" project = '{filters['project']}' "
        for field, value in filters.items():
            if field == 'project': continue
            if field == 'due_date':
                whereclause += f"AND {field} <= '{value}'"
                continue
            whereclause += f"AND {field} = '{value}'"
        query = f"SELECT * from tasks where {whereclause}"
    c.execute(query)
    mytable = from_db_cursor(c)
    mytable.align = "l"
    print(mytable)
    con.commit()
    con.close()
    return c

def changeTaskProject(id, project):
    c.execute(f"UPDATE tasks SET project = '{project}' where rowid = '{id}'")
    con.commit()
    con.close()

def getTask(id):
    res = c.execute(f"""
        SELECT rowid, * from tasks where rowid = {id}
    """).fetchone()
    con.commit()
    con.close()
    return res
