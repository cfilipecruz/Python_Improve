ligh = 0
heavy = 0

for c in range(1, 6):
    weight = float(input('Enter the weight for the {}º person: '.format(c)))
    if c == 1:
        heavy = weight
        ligh = weight
    else:
        if weight > heavy:
            heavy = weight
            
        if weight < ligh:
            ligh = weight

print('The lightest value is {}'.format(ligh))
print('The heaviest value is {}'.format(heavy))