
total = 0
for c in range(1, 7):
    number = int(input('Type a number: '))
    if number % 2 == 0:
        total = total + number

print(total)