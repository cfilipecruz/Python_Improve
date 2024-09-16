users_list = list()
heavy_users = list()
light_users = list()
stop = False
p = 0

while not stop:
    user_name = str(input('Enter a name: '))
    user_weight = int(input('Enter a weight: '))
    proceed = str(input('Do you wish to continue? [S/N]')).upper()
    users_list.append(user_name)
    users_list.append(user_weight)

    if proceed in 'Nn':
        stop = True
    if p == 0:
        heavy_users.append(users_list[:])
        light_users.append(users_list[:])
    else:
        if user_weight > heavy_users[0][1]:
            heavy_users.clear()
            heavy_users.append(users_list[:])
        elif user_weight == heavy_users[0][1]:
            heavy_users.append(users_list[:])
        if user_weight < light_users[0][1]:
            light_users.clear()
            light_users.append(users_list[:])
        elif user_weight == light_users[0][1]:
            light_users.append(users_list[:])
    p = p + 1
    users_list.clear()


print(f'Where registered {p} users')
print(f'the most heavy people are: {len(heavy_users)} ', end='')
for i, c in heavy_users:
    print(f'{i}', end='')
print(f'the most light people are: {len(light_users)}')

