import datetime

def cursor_to_dict_list(cursor):
  tasks = []
  cols = [col[0] for col in cursor.description]
  for row in cursor.fetchall():
      tasks.append(dict(zip(cols, row)))
  return tasks

def to_good_date(date):
  try: return datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d %b')
  except: return '-'

def to_good_time(time):
  try: return datetime.datetime.strptime(time, '%H:%M:%S').strftime('%I:%M %p')
  except: return '-'
