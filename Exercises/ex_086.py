numbers = [[],[],[]]

for c in range(0,3):
    for r in range(0,3):
        numbers[c].append(input(f'Type a number to: {[c,r]} '))

for c in range(0, 3):
    for r in range(0, 3):
        print(f'[ {numbers[c][r]:^5} ] ', end='')
    print()

#print(f'[ {numbers[0][0]} ] [ {numbers[0][1]} ] [ {numbers[0][2]} ]')
#print(f'[ {numbers[1][0]} ] [ {numbers[1][1]} ] [ {numbers[1][2]} ]')
#print(f'[ {numbers[2][0]} ] [ {numbers[2][1]} ] [ {numbers[2][2]} ]')