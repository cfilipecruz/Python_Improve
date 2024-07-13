total = count = 0
while True:
    number = int(input('Type a number: '))
    if number == 999:
        break
    count += 1
    total += number

print(f'The sum of {count} numbers is {total}')