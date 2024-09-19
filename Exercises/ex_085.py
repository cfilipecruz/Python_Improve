numbers = [[],[]]

for c in range(0, 3):
    value = int(input('Tell me a number:'))
    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)


print('The pair numbers are: ',end='' )
for c in numbers[0]:
    print(c, end=' ')

print('\nThe odd numbers are: ',end='' )
for c in numbers[1]:
    print(c, end=' ')