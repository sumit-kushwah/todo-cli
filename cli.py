import click
import datetime
import db
from task import Task

# Global variables ============================================================
TODAY = datetime.datetime.now().strftime('%d-%m-%y')
DEFAULT_PROJECT = "inbox"
RECUR_CHOICES = ["daily", "weekly", "weekend", "sunday", "monday"]

# Entry point =================================================================
@click.group()
def cli():
  '''This is your task manager.'''

# Add command =================================================================
@click.command('add')
@click.option('-d', '--description')
@click.option('-p', '--project', default=DEFAULT_PROJECT)
@click.option('-l', '--label', multiple=True)
@click.option('--date', default=TODAY)
@click.option('-r', '--recur', type=click.Choice(
  RECUR_CHOICES, case_sensitive=False)
)
@click.option('-pr', '--priority', type=int)
@click.argument('title')
def Add(title, description, project, label, date, recur, priority):
  '''Add a new task.'''
  task = Task(title, description, date, recur, project, list(label), priority)
  db.createTask(task)

# Update command ==============================================================
@click.command('update')
def Update():
  '''Update a task.'''
  click.echo('update command!!')

# Delete command ==============================================================
@click.command('delete')
@click.argument('id', type=int)
def Delete(id):
  '''Delete a task.'''
  rows = db.deleteTask(id)
  if (rows == 0):
    click.echo(f'No task found with id `{id}`')

# List command ================================================================
@click.command('list')
@click.option('-p', '--project', default=DEFAULT_PROJECT)
def List(project):
  '''List tasks.'''
  filters = {}
  if (project): filters["project"] = project
  tasks = db.getTasks(filters)
  for task in tasks:
    click.echo(f"{task[0]} `{task[1]}`")

# Show command ================================================================
@click.command('show')
@click.argument('id', type=int)
def Show(id):
  '''Show task.'''
  task = db.getTask(id)
  if task:
    click.echo(f"""
    Id: {task[0]}
    Title: {task[1]}
    Description: {task[2]}
    Due Date: {task[3]}
    Recur: {task[4]}
    Project: {task[5]}
    """)
  else:
    print(f"No task found with id `{id}`.")
  

# Reset command ===============================================================
@click.command()
def Reset():
  '''Reset table.'''
  db.createTable()


# Command group ===============================================================
cli.add_command(Add)
cli.add_command(Update)
cli.add_command(Delete)
cli.add_command(List)
cli.add_command(Reset)
cli.add_command(Show)