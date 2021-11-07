def cursor_to_dict_list(cursor):
  tasks = []
  cols = [col[0] for col in cursor.description]
  for row in cursor.fetchall():
      tasks.append(dict(zip(cols, row)))
  return tasks