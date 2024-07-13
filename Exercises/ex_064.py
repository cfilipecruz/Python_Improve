stop = False
number = sum = 0
while not stop:
    number = int(input('Type a number [999 to stop]: '))
    if number == 999:
        stop = True
    else:
        sum += number
print('The sum is: {}'.format(sum))

