while True:
    number = int(input('Choose your multiplication table: '))
    if number < 0:
        break
    for i in range(0, 11):
        print(f'{number} x {i} = {number*i}')
print('Program ended.')