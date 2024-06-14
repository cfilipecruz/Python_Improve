distancy = int(input('How much km?: '))
distancy = distancy * 0.8 if distancy >= 100 else distancy * 1

print('The price of your boarding ticket is {} euros'.format(distancy/2))