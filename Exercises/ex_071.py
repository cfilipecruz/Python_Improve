from random import randint

print(randint(1, 6))

print('=' * 30)
print('Welcome to The Bank'.center(30))
print('=' * 30)
count500 = count200 = count100 = count50 = count20 = count10 = count5 = 0


value = int(input('How much money do you want to raise? '))

while True:
    if value % 500 == 0:
        value -= 500
        count500 += 1
    elif value % 200 == 0:
        value -= 200
        count200 += 1
    elif value % 100 == 0:
        value -= 100
        count100 += 1
    elif value % 50 == 0:
        value -= 50
        count50 += 1
    elif value % 20 == 0:
        value -= 20
        count20 += 1
    elif value % 10 == 0:
        value -= 10
        count10 += 1
    elif value % 5 == 0:
        value -= 5
        count5 += 1

    if value <= 0: break

if count500 != 0:
    print(f'You will raise {count500} 500 bills.')
if count200 != 0:
    print(f'You will raise {count200} 200 bills.')
if count100 != 0:
    print(f'You will raise {count100} 100 bills.')
if count50 != 0:
    print(f'You will raise {count50} 50 bills.')
if count20 != 0:
    print(f'You will raise {count20} 20 bills.')
if count10 != 0:
    print(f'You will raise {count10} 10 bills.')
if count5 != 0:
    print(f'You will raise {count5} 5 bills.')
