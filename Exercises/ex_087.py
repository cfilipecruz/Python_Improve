numbers = [[],[],[]]
pairs = column = line = 0

for c in range(0,3):
    for r in range(0,3):
        numbers[c].append(int(input(f'Type a number to: {[c,r]} ')))

for c in range(0, 3):
    for r in range(0, 3):
        if numbers[c][r] % 2 == 0:
            pairs = pairs + numbers[c][r]
        if r == 2:
            column = column + numbers[c][r]
        if c == 1:
            line = line + numbers[c][r]
        print(f'[ {numbers[c][r]:^5} ] ', end='')
    print()
print(f'The sum pairs numbers are: {pairs}')
print(f'The sum of third column is: {column}')
print(f'The first line is: {line}')
