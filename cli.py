import click
from commands import Add, Update, Delete, List, Move, Reset, Show, ListAll

@click.group(help="This is your task manager")
def cli():
  pass

cli.add_command(Add)
cli.add_command(Update)
cli.add_command(Delete)
cli.add_command(List)
cli.add_command(Move)
cli.add_command(Reset)
cli.add_command(Show)
cli.add_command(ListAll)