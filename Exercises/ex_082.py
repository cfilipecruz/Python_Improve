leave = False
values = []
pairValues = []
oddValues = []

while not leave:
    value = int(input('Type a Value: '))
    values.append(value)
    choice = input('Do you wish to continue? [Y/N] ').upper().strip()[0]
    if choice in 'N':
        leave = True

print(f'Complete list: {values}')
values.sort()
for i, v in enumerate(values):
    if v % 2 == 0:
        pairValues.append(v)
    else:
        oddValues.append(v)
print(f'The list with only pair numbers is: {pairValues}')
print(f'The list with only odd numbers is {oddValues}')