number = int(input('Type a number: '))
print('The factorial of {} is: '.format(number), end='')
total = number
while number >= 1:
    print(f'{number}', end='')
    if number != 1:
        print(' * ', end='')
    number -= 1
    if number != 0:
        total = total * number

print(' = ', total)
