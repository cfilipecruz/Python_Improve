import datetime

birthyear = int(input('Type your birthday year '))

currentYear = datetime.date.today().year
age = currentYear - birthyear

if age <= 9:
    print('You will be in the Mirim Class')
elif age <= 14:
    print('You will be in the Infantil class')
elif age <= 19:
    print('You will be in the Junior class')
elif age <= 20:
    print('You will be in the Senior class')
else:
    print('You will be in the Masters class')
