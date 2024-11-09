people ={'name': 'Filipe', 'sex': 'M', 'age': 26}
print(people)
print(f'{people["name"]} is {people["age"]} years old')

for i in people:
    print(i)

for i, k in people.items():
    print(f'{i} = {k}')

portugal = []
city1 = {'name':'Braga', 'acronym':'brg'}
city2 = {'name':'Porto', 'acronym':'por'}

portugal.append(city1)
portugal.append(city2)

print(city1['name'])
print(city2['acronym'])
print(portugal)
print(portugal[0]['name'])