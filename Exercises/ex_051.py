number = int(input('Type a number: '))
progress = int(input('Type a progress: '))

for c in range(number, (number + 10) * progress, progress):
    print(c,'', end = '')