import datetime

from constants import TODAY, TOMORROW

def cursor_to_dict_list(cursor):
  tasks = []
  cols = [col[0] for col in cursor.description]
  for row in cursor.fetchall():
      tasks.append(dict(zip(cols, row)))
  return tasks

def to_good_date(date):
  if date == TODAY: return 'today'
  if date == TOMORROW: return 'tomorrow'
  try: 
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    days = (dt - datetime.datetime.now()).days
    if days >= 1 and days <= 7: return dt.strftime('%A')
    return dt.strftime('%d %b')
  except: return '-'

def to_good_time(time):
  try: return datetime.datetime.strptime(time, '%H:%M:%S').strftime('%I:%M %p')
  except: return '-'

def nextRecurDate(date, recur):
  if (date > TODAY): return date
  dt = datetime.datetime.strptime(date, '%Y-%m-%d')
  
  while dt < datetime.datetime.now():
    dt = dt + datetime.timedelta(days=int(recur))
  return dt.strftime('%Y-%m-%d')