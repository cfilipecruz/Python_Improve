from random import randint
values = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for c in values:
    print(f'{c}', end=' ')

print(f'\nThe Highest value was: {sorted(values)[0]}')
print(f'The smallest value was: {sorted(values)[-1]}')