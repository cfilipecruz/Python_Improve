exit = False
while not exit:
    print('Choose an option on the calculator menu:')
    print('---' * 2)
    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')
    print('[5] Exit')
    choice = input('Enter your choice: ')

    if choice != '5':
        number1 = int(input('Enter your first number: '))
        number2 = int(input('Enter your second number: '))
        if choice == '1':
            print(f'{number1} + {number2} = {number1 + number2}')
        elif choice == '2':
            print(f'{number1} - {number2} = {number1 - number2}')
        elif choice == '3':
            print(f'{number1} * {number2} = {number1 * number2}')
        elif choice == '4':
            print(f'{number1} / {number2} = {number1 // number2}')
    else:
        exit = True
print('Calculator finished: Thank you!')