value_01 = int(input('Type a value '))
value_02 = int(input('Type another value '))
value_03 = int(input('Type another value '))

print('The highest typed number is: {}'.format(max(value_01, value_02, value_03)))
print('The lowest typed number is: {}'.format(min(value_01, value_02, value_03)))

#or
lowest = value_01
if value_02 < value_03 and value_02 < value_01:
    lowest = value_02
if value_03 < value_01 and value_03 < value_02:
    lowest = value_03

highest = value_01
if value_02 > value_03 and value_02 > value_01:
    highest = value_02
if value_03 > value_01 and value_03 > value_02:
    highest = value_03

print('The highest typed number is: {}'.format(highest))
print('The lowest typed number is: {}'.format(lowest))
