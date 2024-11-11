player = dict()
goals = list()
player['name'] = str(input('Name: '))
player['matches'] = int(input(f'How many matches did {player["name"]} go?: '))
for g in range(0, player['matches']):
    goals.append(int(input(f'Goals in match {g +1}: ')))
player['goals'] = goals
player['total'] = sum(goals)
print('-='*40)
print(player)
print('-='*40)
for k, v in player.items():
    print(f'The field {k} has the value {v}')
print('-='*40)
print(f'The PLayer {player["name"]} played {player["matches"]} matches.')
for k, v in enumerate(player['goals']):
    print(f'\t=> The Goals in Match {k+1}: {v}')
print(f'{player['name']} scored {player['total']} goals')
