name = input('What is your name? ')
print('Hello {:>20} !!'.format(name))
print('Hello {:<20} !!'.format(name))
print('Hello {:^20} !!'.format(name))

number_1= 4
number_2 = int(input('Enter a number: '))

sum = number_1 + number_2
mult = number_1 * number_2
div = number_1 / number_2
divr = number_1 // number_2
exponent = number_1 ** number_2

print('The sum is: {} \n and multiplication i {} \n and division is {:.4f}'.format(sum,mult,div), end=' ')
print("The divr is {} and the exponent is {}".format(div,exponent))