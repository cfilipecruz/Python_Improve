name = str(input('Wich is your full name?: ')).strip() #.strip removes spaces before and after the text

capitalName = name.upper()
print("Capital case name: {}".format(capitalName))
lowerName = name.lower()
print('Lower case name: {}'.format(lowerName))
countName = len(name)
print('Your name has {} letters'.format(countName))
splitname = name.split()
print('Your first name is {} and has {} letters'.format(splitname[0], len(splitname[0])))


