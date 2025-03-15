import time

def textPrettier( a, b, c):
    print('\n')
    print('-'*40)
    print(f'Count from {a} to {b} jumping c in c houses')

def counter(a, b, c):

    if c == 0:
        c = 1
    if a > b:
        c = c * -1

    textPrettier(0, 10, 1)
    for i in range(0, 11):
        print(f' {i} ', end='', flush=False)
        time.sleep(0.1)
    textPrettier(0, 10, 2)
    for i in range(0, 11,  2):
        print(f'{i} ', end='',flush=False)
        time.sleep(0.1)
    textPrettier(a, b, c)
    for i in range(a, b + (1 if c > 0 else -1), c):
        print(f'{i} ', end='',flush=False)
        time.sleep(0.1)
    return '\nCounter done with success'


#Main
print('Welcome, describe the range and the iteraction')
print(counter( int(input('What is the start number: ')), int(input('What is the end number: ')),  int(input('What is the step iteraction: '))))