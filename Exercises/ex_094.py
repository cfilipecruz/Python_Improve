people = above_average = list()
person = dict()
proceed = True
total_ages = age_average = 0
while proceed:
    person['Name'] = (str(input('Name: ')).strip())
    while True:
        person['Sex'] = str(input('Sex [M/F]:')).capitalize()
        if person['Sex'] in 'MmFf':
            break
    person['Age'] = int(input('Age: '))
    while True:
        proceed = input('Do you wish to continue [S/N]: ')
        if proceed in 'SsNn':
            if proceed in 'Nn':
                proceed = False
        break
    people.append(person.copy())
print('-=' * 40)
print(f'A) There {"is" if len(people) == 1 else "are"} {len(people)} person{"s" if len(people) != 1 else ""} in total')
for k, p in enumerate(people):
    for i, v in p.items():
        if i == 'Age':
            total_ages = total_ages + v
    age_average = total_ages / len(people)
print(f'B) The age average is: {age_average}')
print(f'C) Woman on the list are:')
for p in people:
    if p['Sex'] == 'F':
        print(f'\t=> {p["Name"]} ', end='')
print(f'\nD) This people are above the age average: {age_average}')
for k, p in enumerate(people):
    if int(p['Age']) >= age_average:
        print(f'\t=>{p['Name']}')
