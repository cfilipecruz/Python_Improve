houseValue = int(input('Type the value of the house: '))
salary = float(input('Type the salary: '))
years = int(input('Type the number of years: '))
baseSalary = salary * 0.3
totalMonths = years * 12

loan = (houseValue / totalMonths) * 1.5

if loan <= baseSalary:
    print('The loan was acepted')
    print('basesalary is {}'.format(baseSalary))
    print('loan is {} per month'.format(loan))
else:
    print('The loan was not acepted')
    print('basesalary is {}'.format(baseSalary))
    print('loan is {} per month'.format(loan))