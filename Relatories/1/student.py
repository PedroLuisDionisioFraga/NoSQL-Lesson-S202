class Student:
  def __init__(self, name):
    self.name = name

  def presence(self):
    return f"The student {self.name} was present in class"
