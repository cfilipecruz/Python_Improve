name = str(input('What is your name: '))

if name.upper() == 'FILIPE':
    print('You have a nice name {}'.format(name))
elif name.upper() == 'RUI':
    print('You have a normal name {}'.format(name))
else:
    print('Sorry, you have no such name {}'.format(name))

print('But anyway, its a pleasure to finally meeting you')