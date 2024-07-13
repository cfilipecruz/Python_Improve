ageCount = 0
manCount = 0
womanCount = 0
while True:
    print('=' * 30)
    print('Register a New Person'.center(30))
    print('=' * 30)
    age = int(input('Age: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if age >= 18:
        ageCount += 1
    if sex in 'Mm':
        manCount += 1
    else:
        if age < 20:
            womanCount += 1

    choice = str(input('Do you wish to continue? [Y/N]: ')).strip().upper()[0]
    if choice in 'N':
        break

print(f'There is a total of {ageCount} people above 20 years old')
print(f'There is registered {manCount} man')
print(f'There is registered {womanCount} woman below 20 years old')