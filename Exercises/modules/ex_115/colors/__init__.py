def colorfy(text='empty', text_color='white', background=False, background_color='black'):
    color_codes = {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
        'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37
    }

    background_codes = {
        'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
        'blue': 44, 'magenta': 45, 'cyan': 46, 'white': 47
    }

    if background:
        if background_color in ['white', 'yellow', 'cyan']:
            text_color_code = color_codes['black']
        else:
            text_color_code = color_codes['white']

        bg_color_code = background_codes.get(background_color, 40)
        return f'\033[{text_color_code};{bg_color_code}m{text}\033[0m'

    text_color_code = color_codes.get(text_color, 37)
    return f'\033[{text_color_code}m{text}\033[0m'
