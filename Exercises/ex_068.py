import random
count = 0

while True:
    pc = random.randrange(1, 10)
    number = int(input('Type a number: '))
    choice = str(input('Pair or Odd [PAIR/ODD]: ')).upper().strip()
    total = pc + number
    if total % 2 == 0:
        result = 'PAIR'
    else:
        result = 'ODD'

    print(f'Pc choose {pc} and you choose {number} -> {pc} + {number} = {total}, so its {result}')
    if result != choice:
        break
    count += 1

print(f'The game finished with {count} victories')