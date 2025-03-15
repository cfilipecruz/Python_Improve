def record(n='Unknown', g=0):
    return f'Name: {n} has {g} Goals '

print('-'*30)
name = str(input('PLayers Name: '))
goals = str(input('Players Goals: '))

if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

if name.strip() == '':
    print(record(g=goals))
else:
    print(record(name, goals))

