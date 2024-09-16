values = []

for c in range(0, 6):
    values.append(int(input('Type a Value: ')))

print(f'Your new list is: {values}')
print(f'\nThe highest value in the list is {max(values)} in position', end='')
for i, v in enumerate(values):
    if v == max(values):
        print(i, end='')
    else:
        print('.', end='')

print(f'\nThe smallest value in the list is {min(values)} in position', end='' )


for i, v in enumerate(values):
    if v == min(values):
        print(i, end='')
    else:
        print('.', end='')