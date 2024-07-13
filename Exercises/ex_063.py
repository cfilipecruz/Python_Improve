terms = int(input('How many terms do you need?: '))
count = 0
n1 = 0
n2 = 1

print('The Fibonacci sequence is: ')

while count < terms:
    if count == 0:
        total = n1
    else:
        total = n2 + n1
    print(total, '->', end=' ')
    n1 = n2
    n2 = total
    count += 1

print('End!')