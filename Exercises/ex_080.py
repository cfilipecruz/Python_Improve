leave = False
count = 0
values = []

while not leave:
    count += 1
    value = int(input('Type a number: '))
    if value not in values:
        if len(values) < 1 or value > max(values): #if first value add to the array
            values.append(value)
        else:
            for i in range(0, len(values)):
                if value < values[i]:
                    values.insert(i, value)
                    break
        print('Value added to the list')
    else:
        count -= 1
        print('Value already exists, type again')
    if count >= 5:
        leave = True

print('=' * 40)
print(f'The values are: {values}')