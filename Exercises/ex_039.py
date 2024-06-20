import datetime
year = int(input('What is your birthday year? '))

currentYear = datetime.date.today().year

age = currentYear - year

if age < 18:
    remainingTime = 18 - age
    print('You are not ready for army yet, come back later in {} years.'.format(remainingTime))
elif 18 <= age <= 20:
    print('You are ready for army, go to your near base.')
else:
    overdueTime = (20 - age)*-1
    print('You have expired the army application by {} years.'.format(overdueTime))