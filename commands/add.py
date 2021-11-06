import click, db
from task import Task
from constants import DEFAULT_PROJECT, DATE_FORMATS, TODAY, RECUR_CHOICES

@click.command('add', help="Add a new task.")
@click.option('-n', '--note')
@click.option('-p', '--project', default=DEFAULT_PROJECT)
@click.option('-d', '--date', default=TODAY, type=click.DateTime(formats=DATE_FORMATS))
@click.option('-r', '--recur', type=click.Choice(
  RECUR_CHOICES, case_sensitive=False)
)
@click.argument('title')
def Add(title, note, project, date, recur):
  task = Task(title, note, date, recur, project)
  db.createTask(task)