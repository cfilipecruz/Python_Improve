from ..colors import colorfy


def display():
    menu = {
            1: 'Check Registered Users',
            2: 'Register New User',
            3: 'Exit Application'
    }

    print(colorfy('-', 'white') * 40)
    print(colorfy('Main Menu', 'magenta').center(40))
    print(colorfy('-', 'white') * 40)
    for c, v in menu.items():
        print(colorfy(f'{c}', 'yellow'), end='')
        print(colorfy(f' - ', 'white'), end='')
        print(colorfy(f'{v}', 'blue'))
    print(colorfy('-', 'white') * 40)
