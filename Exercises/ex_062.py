number = int(input('What is the first number: '))
progression = int(input('What is the progression number: '))
terms = 10
more = False
count = 0
addMore = 0
start = number
while not more:
    end = start + (terms * progression)
    for c in range(start, end, progression):
        print(f'{c} -> ', end='')
        count += 1
    print('Break')
    terms = int(input('How many more terms you want to show?: '))
    start = end
    if terms == 0:
        more = True
print('Program ended with {} terms printed.'.format(count))