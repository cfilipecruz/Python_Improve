from class_022 import numbers

num = int(input('Type a number: '))

fat = numbers.fatorial(num)
double = numbers.double(num)
triple = numbers.triple(num)

print(f'The Factoral of {num} is {fat}')
print(f'The double of {num} is {double}')
print(f'The triple of {num} is {triple}')