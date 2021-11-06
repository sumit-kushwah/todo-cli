import click, db
from constants import DATE_FORMATS, TODAY, DEFAULT_PROJECT

@click.command('list', help="List tasks.")
@click.option('--date', default=TODAY, type=click.DateTime(formats=DATE_FORMATS))
@click.option('-a', '--all', is_flag=True)
@click.option('-p', '--project', default=DEFAULT_PROJECT)
def List(project, date, all):
  filters = {}
  if (project): filters["project"] = project
  if (date): filters["date"] = date
  db.getTasks(filters, all)