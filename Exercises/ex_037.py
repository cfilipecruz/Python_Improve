import numbersystem

number = int(input('Type a number: '))
print('-=-' * 30)
print('Choose an option')
print('1 to Binary')
print('2 to Octal')
print('3 to Hexadecimal')
print('-=-' * 30)
choice = int(input('Type a number: '))

if choice == 1:
    converted = numbersystem.decimalToBinary(number)
    print(f'{converted} in Binary.')
    #bin(number)
elif choice == 2:
    converted = numbersystem.decimalToOctal(number)
    print(f'{converted} in Octal.')
    #oct(number)
else:
    converted = numbersystem.decimalToHexa(number)
    print(f'{converted} in Hexadecimal.')
    #hex(number)