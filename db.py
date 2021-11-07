import sqlite3

from helper import cursor_to_dict_list
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('todo.db')
        self.cursor = self.connection.cursor()

    def createTable(self):
        self.cursor.execute("DROP TABLE tasks")
        self.cursor.execute("""CREATE TABLE tasks (
            title TEXT NOT NULL,
            date TEXT,
            time TEXT,
            recur TEXT,
            project TEXT,
            is_completed BOOL
        )""")

    def createTask(self, task):
        self.cursor.execute("INSERT INTO tasks VALUES(?, ?, ?, ?, ?, ?)", task.to_db_tuple())

    def deleteTask(self, id):
        res = self.cursor.execute(f"""
            DELETE FROM tasks where rowid = {id}
        """).rowcount
        return res

    def getTasks(self, date, project="inbox", completed=False):
        query = f"""SELECT rowid, * 
                        from tasks 
                where project = '{project}' 
                    AND date <= '{date}'
                    AND is_completed = '{int(completed)}'
                """
        self.cursor.execute(query)
        return cursor_to_dict_list(self.cursor)
    
    def getAllTasks(self, find="", completed=False):
        query = f"""SELECT rowid, * 
                        from tasks 
                    where is_completed = '{int(completed)}'
                    AND (
                        title LIKE '%{find}%'
                        OR date LIKE '%{find}%'
                        OR time LIKE '%{find}%'
                        OR recur LIKE '%{find}%'
                        OR project LIKE '%{find}%'
                    )
                """
        self.cursor.execute(query)
        return cursor_to_dict_list(self.cursor)

    def changeTaskProject(self, id, project):
        self.cursor.execute(f"UPDATE tasks SET project = '{project}' where rowid = '{id}'")

    def getTask(self, id):
        res = self.cursor.execute(f"""
            SELECT rowid, * from tasks where rowid = {id}
        """).fetchone()
        return res

    def __del__ (self):
        self.connection.commit()
        self.connection.close()
