def readint():
    line = ''
    while True:
        number = str(input('Type a number: ')).replace(',','.',1)
        if number.replace('.', '1', 1).isnumeric():
            number = float(number)
            if number % 1 == 0:
                line = f'The number {number} is an integer'
                break
            else:
                line = f'The number {number} is a float'
                break
        else:
            print('\033[0;31mYou need to type a number.\033[m')
    return line


print(readint())

