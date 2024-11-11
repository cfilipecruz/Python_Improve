import random
from time import sleep
from operator import itemgetter
value = dict()
values = list()

for c in range(0,5):
    sort = random.randint(1,6)
    value['player'] = c
    value['value'] = sort
    values.append(value.copy())

print('=' * 40)
print('Sorted Values')
sleep(0.5)
for e in values:
    print(f'The player {e['player']} took {e['value']}')
    sleep(0.5)
print('='*40)
print('Ranking of players')

#sorted_values = sorted(values, key=lambda k: k['value']) !!IMPORTANT!! using lmabda gives
# more flexibility,
# we can use for example  k['value'].lower() to ignore case sensitivity,
# but is usualy slower.

sorted_values = sorted(values, key=itemgetter(1)) #1 being the dict value, its more efficient than lambda

for i, e in enumerate(sorted_values):
    print(f'In {i + 1}º place we have player number {e['player']} took {e['value']}')
    sleep(0.5)