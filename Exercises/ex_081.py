leave = False
values= []
while not leave:
    print('-' * 40)
    value = int(input('Type a value: '))
    values.append(value)
    choice = str(input('Do you wish to continue? [Y/N]')).upper().strip()[0]

    if choice == 'N':
        leave = True
print(f'You typed {len(values)} values.')
values.reverse()
print(f'The values in opposite order: {values}')
if 5 in values:
    print(f'5 is part of the list')
else:
    print(f'5 is not part of the list')
