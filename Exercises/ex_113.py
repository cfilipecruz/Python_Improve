while True:
    try:
        integer = int(input('Type an integer number: '))
    except KeyboardInterrupt:
        print('\033[41mERROR: The user interrupted the program')
    except (ValueError, TypeError):
        print('\033[41mERROR: You need to type an integer number.')
    else:
        break

while True:
    try:
        real = float(input('Type an real number: ').strip().replace(',', '.'))
    except KeyboardInterrupt:
        print('\033[41mERROR: The user interrupted the program')
    except (ValueError, TypeError):
        print('\033[41mERROR: You need to type an real number.')
    else:
        break

print(f'The Integer number is {integer}')
print(f'The Real number is {real}')