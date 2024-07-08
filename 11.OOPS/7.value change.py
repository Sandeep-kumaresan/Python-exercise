class student:
    student_name="Sundar Pichai"
    marks=99
"""print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, 'student_name', 'Angel Brooks')
setattr(Student, 'marks', 95) 
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")"""
stu=student()
print("Oldname:",stu.student_name)
print("Oldmark:",stu.marks)
student.student_name="Elon musk"
student.marks=100
print("Newname:",stu.student_name)
print("Newmark:",stu.marks)