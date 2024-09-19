import random
import time
numbers = []
previous = []
print('-'*25)
print(f'{'Play on Jackpot':^25}')
print('-'*25)


number = int(input('How many lists you want to generate?'))

print('Generating possible jackpots')

for i in range(number):
    j = 0
    while j != 6:
        generated = random.randint(1,60)
        if generated not in numbers:
            numbers.append(generated)
            j += 1
    numbers.sort()
    print(f'Jackpot number {i+1}: {numbers}')
    previous.append(numbers[:])
    numbers.clear()
    time.sleep(1)