def fatorial(a, b = False):
    """
    Calculate the Factorial of a number.
    Parameters:
        a = number
        b = True of False
    """
    result = 1
    if a > 0:
        print(f'{a}! = ', end='')
        for i in range(a, 0, -1):
            result = result * i
            if b == True:
                print(f' {i}', end='')
                if i > 1:
                    print(f' x', end='')
        if b == True:
            print(f' = ', end='')
        print(f'{result}')
    else:
        print(f'The value has to be above zero')


fatorial(4, False)
help(fatorial)