

def get_help(line):
    ui(f'Command ""{line}""', 'blue', 'title')
    ui('', 'white', 'text')
    help(line)
    ui('', 'white', 'text')


def ui(text, color, type):
    code = 1
    end_code = '\033[m'
    if color == 'blue':
        code = '\033[104m\033[30m'
    elif color == 'green':
        code = '\033[102m\033[30m'
    elif color == 'red':
        code = '\033[41m'
    elif color == 'white':
        code = '\033[7m'
    else:
        code = '\033[m'

    if type == 'title':
        size = len(text)
        print(f'{code}=' * (size + 10))
        print(f'{text}'.center(size + 10))
        print(f'{code}=' * (size + 10))
        print(f'{end_code}', end='')

    elif type == 'text':
        print(f'{code}')
        print(f'{text}', end='')
    else:
        print(f'Wrong Parameters')


while True:
    ui('** Get Help **', 'green', 'title')
    user_input = str(input('Which Library would you Like to check (type exit to end): ')).strip().lower()

    if user_input in 'exit':
        ui('** Program Ended **', 'red', 'title')
        break

    get_help(user_input)


