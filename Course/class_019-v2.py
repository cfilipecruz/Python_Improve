city = dict()
portugal = list()
for c in range(0,2):
    city['name'] = str(input(f'What is the city number {c}?: '))
    city['colorFlag'] = str(input('What is the color of that city?: '))
    portugal.append(city.copy())

for e in portugal:
    for i, v in e.items():
        print(f'{i}: {v}')