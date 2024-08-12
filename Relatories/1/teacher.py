class Teacher:
  def __init__(self, name):
    self.name = name

  def teach_class(self, topic):
    return f"The teacher {self.name} was teaching {topic} to the class"
