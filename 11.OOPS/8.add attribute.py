class student:
    student_id=10
    student_name="harry"

for key,value in student.__dict__.items():
    if not key.startswith('_'):
        print(key,":",value)

student.student_class = "Good"

for key,value in student.__dict__.items():
    if not key.startswith('_'):
        print(key,":",value)

del student.student_id

for key,value in student.__dict__.items():
    if not key.startswith('_'):
        print(key,":",value)