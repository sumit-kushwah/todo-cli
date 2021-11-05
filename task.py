class Task:
  
  def __init__(
    self, 
    title, 
    description = None,
    due_date = None,
    recur = None,
    project = None,
    labels = None,
    priority = None,
    completed_date = None
    ):
    self.title = title
    self.description = description
    self.due_date = due_date
    self.recur = recur
    self.project = project
    self.labels = labels
    self.priority = priority
    self.completed_date = completed_date

  def to_db_tuple(self):
    t = (
      self.title,
      self.description,
      self.due_date,
      self.recur,
      self.project,
      str(self.labels),
      self.priority,
      self.completed_date
    )
    return t

    