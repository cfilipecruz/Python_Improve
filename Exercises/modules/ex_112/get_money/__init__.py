def clear():
    while True:
        value = str(input('Enter a value: ').replace(',','.').strip())
        if value.isalpha() or value == "" or value.isnumeric():
            print(f'"{value}" is not a number, please enter a numeric value')
        else:
            return float(value)
            break

