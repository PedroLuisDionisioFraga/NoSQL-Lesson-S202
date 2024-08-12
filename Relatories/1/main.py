from student import Student
from teacher import Teacher
from classroom import Classroom

teacher = Teacher("Lucas")
student1 = Student("Maria")
student2 = Student("Pedro")
classroom = Classroom(teacher, "Programação Orientada a Objetos")
classroom.add_student(student1)
classroom.add_student(student2)
print(classroom.attendance_list())
