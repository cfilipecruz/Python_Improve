import random

firstStudent = str(input('First student: '))
secondStudent = str(input('Second student: '))
thirdStudent = str(input('Third student: '))
fourthStudent = str(input('Fourth student: '))

studentList = [firstStudent, secondStudent, thirdStudent, fourthStudent]
random.shuffle(studentList)

print(studentList)
