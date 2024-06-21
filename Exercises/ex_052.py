number = int(input('Type a number: '))
count = 0

for c in range(1, number + 1):
    if number % c == 0:
        count = count + 1
        print('\033[33m', c, end='')
    else:
        print('\033[31m', c , end='')

print('\n\033[m The Number {} its divisive {} times'.format(number, count))

if count <= 2:
    print('The number', number, 'is a prime number.')
else:
    print('The number', number, 'is not a prime number.')
