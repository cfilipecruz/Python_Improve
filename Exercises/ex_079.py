leave = False
values = []
while not leave:
    value = int(input('Type a number: '))
    if values.count(value):
        print('Value already exists, not added.')
    else:
        print('Value added with success')
        values.append(value)
    choice = str(input('Do you want to try again? [y/n]: ')).strip().upper()[0]
    if choice == 'N':
        leave = True
values.sort()
print(values)