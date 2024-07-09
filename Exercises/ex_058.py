import random

pcNumber = random.randint(1, 10)
counter = 1
userNumber = int(input('Guess the number: '))
while pcNumber != userNumber:
    counter += 1
    userNumber = int(input('Wrong number, try again: '))

print(f'You guessed the number in {counter} atempt(s).')