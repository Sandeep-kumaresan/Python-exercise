class student:
    pass
class marks:
    pass

student1 = student()
mark1=marks()
print(isinstance(mark1,marks))
print(isinstance(student1,student))
print(isinstance(mark1,student))
print(isinstance(student1,marks))
print(issubclass(student,object))
print(issubclass(marks,object))