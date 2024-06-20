firstExam = float(input('What is your first exam classification: '))
secondExam = float(input('What is your second exam classification: '))

average = (firstExam + secondExam)/ 2

if average < 5:
    print('You have failed the class')
elif 5 <= average <= 7:
    print('You have to recover your grade')
else:
    print('You have passed the class')