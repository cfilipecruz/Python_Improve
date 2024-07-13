from random import randint

print('=' * 30)
print('Welcome to The Bank'.center(30))
print('=' * 30)
count = [500, 200, 100, 50, 20, 10, 5]
bills = [0, 0, 0, 0, 0, 0, 0]

value = int(input('How much money do you want to raise? '))

while True:
    for c in range(0,len(count)):
        if value % count[c] == 0:
            value -= count[c]
            bills[c] += 1
            break
    if value <= 0: break

for c in range(0,len(bills)):
    print(f'You are raising {count[c]} bills of {bills[c]} ')