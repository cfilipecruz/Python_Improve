def increase(number=0, increase=1, formating=False):
    """
    Increases a given number by a specified value.

    :param number: The original number (default is 0).
    :param increase: The value to add to the number (default is 1).
    :param formating: If True, returns the formatted value as a string (default is False).
    :return: The increased value, formatted if requested.
    """
    print(f'The Increasing number by {increase}')
    answer = number + increase
    return answer if not formating else format(answer)


def decrease(number=0, decrease=1, formating=False):
    """
    Decreases a given number by a specified value.

    :param number: The original number (default is 0).
    :param decrease: The value to subtract from the number (default is 1).
    :param formating: If True, returns the formatted value as a string (default is False).
    :return: The decreased value, formatted if requested.
    """
    print(f'Decreasing number by {decrease}')
    answer = number - decrease
    return answer if not formating else format(answer)


def double(number=0, formating=False):
    """
    Doubles the given number.

    :param number: The original number (default is 0).
    :param formating: If True, returns the formatted value as a string (default is False).
    :return: The doubled value, formatted if requested.
    """
    print('Doubling...')
    answer = number * 2
    return answer if not formating else format(answer)


def half(number=0, formating=False):
    """
    Halves the given number.

    :param number: The original number (default is 0).
    :param formating: If True, returns the formatted value as a string (default is False).
    :return: Half of the original value, formatted if requested.
    """
    print('Halfing?...')
    answer = number / 2
    return answer if not formating else format(answer)


def format(number=0, coin='€'):
    """
    Formats a number to two decimal places and adds a currency symbol.

    :param number: The number to format (default is 0).
    :param coin: The currency symbol to append (default is '€').
    :return: The formatted string with two decimal places and currency symbol.
    """
    return f'{number:.2f}{coin}'.replace('.', ',')