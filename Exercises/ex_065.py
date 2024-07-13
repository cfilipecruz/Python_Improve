start = count = total =0
end = False
while not end:
    value = int(input('Type a number: '))
    if count == 0:
        highest = lowest = value
    else:
        if value > highest:
            highest = value
        if value < lowest:
            lowest = value
    total += value
    user = str(input('Do you wish to continue? [s/n]: '))
    if user == 'n':
        end = True
    count += 1
print('You typed {} numbers and its average was {} '.format(count, total/count))
print('The highest value was {} and the lowest value was {}'.format(highest, lowest))