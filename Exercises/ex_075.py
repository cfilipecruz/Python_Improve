numbers = (int(input('Type a value: ')), int(input('Type another value: ')), int(input('Type another value: ')), int(input('Type  another value: ')))
print(numbers)
count = 0

print(f'The value 4 appeared {numbers.count(4)} times')
if numbers.count(3) > 0:
    print(f'The number 3 appeared in position {numbers.index(3) + 1}')

for c in numbers:
    if c % 2 == 0:
        count += 1
if count > 0:
    print(f'The pair numbers are: {count} ')