from constants import FUTURE_COLOR, PAST_COLOR, PRESENT_COLOR, TODAY

class Task:
  def __init__(
    self, 
    title, 
    date = None,
    time = None,
    recur = None,
    project = None,
    id = None,
    is_completed = False
    ):
    self.title = title
    self.date = date
    self.time = time
    self.recur = recur
    self.project = project
    self.id = id
    self.is_completed = is_completed

  def to_db_tuple(self):
    t = (
      self.title,
      self.date,
      self.time,
      self.recur,
      self.project,
      self.is_completed
    )
    return t

  def to_list(self, fields):
    items = []
    for field in fields:
      items.append(self.getColor() + self.getFieldValue(field))
    return items

  def getFieldValue(self, field):
    result = None
    if (field == 'title'):
      result = self.title
    if (field == 'date'):
      result = self.date
    if (field == 'time'):
      result = self.time
    if (field == 'recur'):
      result = self.recur
    if (field == 'project'):
      result = self.project
    if (field == 'rowid'):
      result = self.id
    if result: return str(result)
    return '-'
    
  
  def getColor(self):
    if self.date < TODAY: return PAST_COLOR
    if self.date > TODAY: return FUTURE_COLOR
    return PRESENT_COLOR

    