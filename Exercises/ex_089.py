student_grades = [[], [], [], []]
students = []
student_number = 0
while True:
    student_number += 1
    student_grades[0] = int(student_number)
    student_grades[1] = str(input('Name: ')).capitalize()
    student_grades[2] = float(input('First Grade: '))
    student_grades[3] = float(input('Second Grade: '))
    students.append(student_grades[:])
    choice = str(input('Do you wish to continue? [S/N]: ')).upper().strip()[0]
    if choice in 'nN':
        break

print('-'*30)
for n in students:
    media = (n[2] + n[3])/2
    print(f'Student {n[0]} : {n[1]} : {media}')
print('-'*30)

while True:
    select_student = int(input('Select student number, 999 to end the program:'))
    if select_student == 999:
        break
    if select_student <= len(students):
        for n in students:
            if n[0] == select_student:
                print(f'Student number select_student is {n[1]}')
                print(f'Grades are: {n[2]}, {n[3]}')