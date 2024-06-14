velocity = int(input('What is the velocity of your car?: '))

if velocity <= 120:
    print('You are on a normal velocity')
else:
    velocity = velocity - 120
    velocity = velocity * 3
    print('You exceed in the velocity, You will take {}€ traffic ticket'.format(velocity))