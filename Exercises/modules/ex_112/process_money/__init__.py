def get(number=0, increase=1, decrease=0):
    increasing = number + increase
    decreasing = number - decrease
    doubling = number * 2
    halfing = number / 2

    print('*'*40)
    print('Data'.center(40))
    print('*' * 40)
    print(f'Price:', end='')
    print(f'{format(number)}'.rjust(40-len('Price')))
    print(f'Increased Value:', end='')
    print(f'{format(increasing)}'.rjust(40-len('Increased Value')))
    print(f'Decreased Value:', end='')
    print(f'{format(decreasing)}'.rjust(40-len('Decreased Value')))
    print(f'Doubling Value:', end='')
    print(f'{format(doubling)}'.rjust(40-len('Doubling Value')))
    print(f'Halfing Value:', end='')
    print(f'{format(halfing)}'.rjust(40-len('Halfing Value')))
    print('*'*40)


def format(number=0, coin='€'):
    return f'{number:.2f}{coin}'.replace('.', ',')