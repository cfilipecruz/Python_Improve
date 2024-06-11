import random

firstStudent = str(input('First Student: '))
secondStudent = str(input('Second Student: '))
thirdStudent = str(input('Third Student: '))
fourthStudent = str(input('Fourth Student: '))

list = [firstStudent, secondStudent, thirdStudent, fourthStudent]

print('The choosen student is {}'.format(list[random.randrange(1, 4)]))
