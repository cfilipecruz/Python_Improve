from random import randint
from time import sleep

print('-=-' * 20)
print('I am Thinking in a number from 1 to 5')
print('-=-' * 20)
usernumber = int(input('Guess the number: '))
print('Processing')
sleep(3)
pcnumber = randint(1, 5)
if usernumber == pcnumber:
    print('You guessed the Number!')
else:
    print('The correct answer was {}'.format(pcnumber))
    print('You guessed the Number wrong! Try again!')

