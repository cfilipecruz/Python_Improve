from time import sleep
import datetime
current_year = datetime.date.today().year
person = dict()
person['name'] = str(input('What is your name?: '))
person['age'] = current_year - int(input('What is your birthday year?: '))
person['Work Permit'] = str(input('What is your work permit code?: ')).upper().strip()
verified = True
print('Verifying work permit.')
#  Imagine a function to validate the working permit code, for exercise I will not.
sleep(1)
if len(person['Work Permit']) == 5:
    if verified:
        print('The work permit code was Validated.')
        print('=' * 30)
        person['year_of_contract'] = int(input('When you were hired(year): '))
        if person['year_of_contract'] == current_year + 1:
            print('The year of contract is invalid.')
        else:
            person['salary'] = float(input('How much are you payed for:'))
            person['Total Salary'] = (person['salary'] * 12) * (current_year - person['year_of_contract'])
            person['Years to retirement'] = (current_year - person['year_of_contract']) + 40
            for p in person.items():
                print(f'{p[0]}: {p[1]}')
            print('=' * 30)
    else:
        print('Work permit does not exist.')
else:
    person[person['permit']] = 'Invalid'
    print('Work permit code is invalid.')
    print('='*30)
    for p in person.items():
        print(f'{p[0]}: {p[1]}')
    print('=' * 30)
    print('Have a great day.')
#If you are reading this, this was taken from github https://github.com/cfilipecruz