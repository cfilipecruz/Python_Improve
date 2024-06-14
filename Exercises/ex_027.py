name = str(input("What is your name? ")).strip().split()

print('Your first name is {}'.format(name[0]))
print('Your last name is {}'.format(name[-1]))

#or

print('Your first name is {}'.format(name[0]))
print('Your last name is {}'.format(name[len(name) - 1]))