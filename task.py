class Task:
  is_completed = False

  def __init__(
    self, 
    title, 
    note = None,
    due_date = None,
    recur = None,
    project = None,
    ):
    self.title = title
    self.note = note
    self.date = due_date
    self.recur = recur
    self.project = project

  def to_db_tuple(self):
    t = (
      self.title,
      self.note,
      self.date,
      self.recur,
      self.project,
      self.is_completed
    )
    return t

    