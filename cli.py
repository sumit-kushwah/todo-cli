import click
from commands import Add, Update, Delete, List, Move, Reset, Show, ListAll
from db import Database

@click.group(invoke_without_command=True, help="This is your task manager")
@click.option('-d', '--delete', multiple=True)
@click.option('-c', '--complete', multiple=True)
def cli(delete, complete):
  for id in delete:
    db = Database()
    db.deleteTask(id)

cli.add_command(Add)
cli.add_command(Delete)
cli.add_command(List)
cli.add_command(Move)
cli.add_command(Reset)
cli.add_command(ListAll)