import click
import db

@click.command('delete', help="Delete a task.")
@click.argument('id', type=int)
def Delete(id):
  rows = db.deleteTask(id)
  if (rows == 0):
    click.echo(f'No task found with id `{id}`')