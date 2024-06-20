import random
items = ('Rock', 'Paper', 'Scissor')

print('Your options')
print('[0]', items[0])
print('[1]', items[1])
print('[2]', items[2])
option = int(input('Enter your choice: '))
print('Jo')
print('Ken')
print('Po!!!')

pcChoice = random.randint(0, 3)
print('Pc choose ', items[pcChoice])

if option == 0 and pcChoice == 0 or option == 1 and pcChoice == 1 or option == 2 and pcChoice == 2:
    print('Tie')
elif option == 0 and pcChoice == 2 or option == 1 and pcChoice == 0 or option == 2 and pcChoice == 1:
    print('You win!')
elif option == 1 and pcChoice == 2 or option == 2 and pcChoice == 0 or option == 0 and pcChoice == 1:
    print('You lose!')
else:
    print('Choose a valid option')

