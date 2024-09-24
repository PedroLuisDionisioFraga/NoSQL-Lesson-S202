class Passenger:
  def __init__(self, name:str, document:str):
    self.name = name
    self.document = document

  def dict(self):
    return {"name": self.name, "document": self.document}
