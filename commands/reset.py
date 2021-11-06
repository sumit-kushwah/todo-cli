import click, db

@click.command('reset', help="Reset Table")
@click.confirmation_option(prompt="Are you sure?")
def Reset():
  db.createTable()