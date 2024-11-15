player = dict()
goals = list()
players = list()
cycle = True
while cycle:
    player['name'] = str(input('Name: '))
    player['matches'] = int(input(f'How many matches did {player["name"]} go?: '))
    for g in range(0, player['matches']):
        goals.append(int(input(f'Goals in match {g + 1}: ')))
    player['goals'] = goals[:]
    player['total'] = sum(goals)
    print('-='*40)
    players.append(player.copy())
    goals.clear()
    while True:
        action = str(input('Do you wish to continue? [Y/N]: ')).upper().strip()[0]
        if action in 'YN':
            if action == 'N':
                cycle = False
            break
print('-' * 40)
print(f"{'Code':<10}{'Name':<10}{'Goals':<10}{'Total':<10}")
print('','-' * 40)
for e, p in enumerate(players):
    print(f"{f'{e+1}':<10}{f'{p['name']}':<10}{f'{p['goals']}':<10}{f'{p['total']}':<10}")
print('', '=-' * 40)
cycle = True
while cycle:
    while True:
        which_player = int(input('Which player do you wish to show? [999 to exit]: '))
        if which_player == 999:
            cycle = False
            break
        else:
            if which_player <= len(players) and which_player > 0:
                for e, p in enumerate(players):
                    if e == which_player - 1:
                        print(f'Player: {p["name"]}')
                        for eg, g in enumerate(p['goals']):
                            print(f'In game {eg+1} did: {g} goals')
                break
            else:
                print('Please enter a valid player number.')
