import click
from tabulate import tabulate
from commands.helper import tabulateList
from db import Database
from task import Task

@click.command('listall', help="List All tasks.")
@click.option('--completed', is_flag=True)
@click.option('-f', '--find', default="")
def ListAll(find, completed):
  db = Database()
  items = db.getAllTasks(find, completed)
  if len(items) > 0:
    tasks = []
    for item in items:
      task = Task(item['title'], item['date'], item['time'], item['recur'], item['project'], item['rowid'], item['is_completed'])
      tasks.append(task.to_list(['rowid', 'title', 'date', 'time', 'recur', 'project']))
    headers = ["Id", "Title", "Date", "Time", "Recur", "Project"]
    tabulateList(tasks, headers)
