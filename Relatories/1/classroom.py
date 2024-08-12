from student import Student
from teacher import Teacher

class Classroom:
  def __init__(self, teacher, topic):
    self.students = []
    self.teacher = teacher
    self.topic = topic

  def add_student(self, student):
    self.students.append(student)

  def attendance_list(self):
    print(f"Presença na aula sobre {self.topic}, ministrada pelo professor {self.teacher.name}:")
    presence_list = [f"O aluno {student.name} está presente." for student in self.students]
    return "\n".join(presence_list)
