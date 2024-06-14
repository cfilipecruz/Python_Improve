number = int(input('Type a number: '))
numbers = str(number).zfill(10) # fill if there lack of numbers
print(len(numbers))

print('''
        Unidades: {}
        Dezenas: {}
        Centenas: {}
        Milhares: {}
      '''.format(numbers[-1], numbers[(len(numbers))+1], numbers[(len(numbers))-2], numbers[(len(numbers))-3]))

#or

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('''
        Unidades: {}
        Dezenas: {}
        Centenas: {}
        Milhares: {}
      '''.format(u, d, c, m))
