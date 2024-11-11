person = dict()
person['name'] = str(input('Name: '))
person['average'] = int(input('Average: '))

print(f'The person name is {person["name"]}')
print(f'The person average is {person["average"]}')
if person['average'] < 10:
    print('The person failed the class')
else:
    print('The person succeeded')
