import class_022_utils

num = int(input('Type a number: '))

fat = class_022_utils.fatorial(num)
double = class_022_utils.double(num)
triple = class_022_utils.triple(num)

print(f'The Factoral of {num} is {fat}')
print(f'The double of {num} is {double}')
print(f'The triple of {num} is {triple}')