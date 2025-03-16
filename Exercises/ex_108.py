from modules import ex_107

number = int(input('Enter a value: '))
print(f'The increase of {ex_107.format(number, '€')} is {ex_107.format(ex_107.increase(number, 5))}')
print(f'The decrease of {ex_107.format(number, '€')} is {ex_107.format(ex_107.decrease(number, 5))}')
print(f'The double of {ex_107.format(number,'€')} is {ex_107.format(ex_107.double(number))}')
print(f'The half of {ex_107.format(number, '€')} is {ex_107.format(ex_107.half(number))}')