sexualOrientation = str(input('Inform your sexual orientation [M/F]: ')).upper().strip()[0]
while sexualOrientation not in 'MmFf':
    if sexualOrientation not in 'Mm' or sexualOrientation not in 'fF':
        print('That is not a valid sexual Orientation, please use M or F')
    sexualOrientation = str(input('Inform your sexual orientation [M/F]: ')).upper().strip()[0]


print('Thank you for the information')