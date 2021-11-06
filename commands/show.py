import click, db

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