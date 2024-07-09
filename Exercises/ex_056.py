total = 0
numberOfPeople = 3
olderAge = 0
olderName = ''
womanCount = 0
for c in range (1, numberOfPeople + 1):
    print('--- Person {}'.format(c), ' ---')
    name = str(input('Name: '))
    age = int(input('Age: '))
    sexualOrientation = input('Sexual Orientation [M/F]: ').upper().strip()
    total += age
    if sexualOrientation == 'M':
        if c == 1:
            olderAge = age
            olderName = name
        elif age > olderAge:
            olderAge = age
            olderName = name
    else:
        if age < 20:
            womanCount += 1

print('The age average is {}'.format(total/numberOfPeople))
print('The oldest person is {} with {} years old'.format(olderName,olderAge))
print('There are {} woman below 20 years'.format(womanCount))

