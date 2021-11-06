import click, db

@click.command('move', help="Move task to a project.")
@click.argument('id', type=int)
@click.argument('project', type=click.STRING)
def Move(id, project):
  db.changeTaskProject(id, project)