a = 5
b = 6

print('The values are \033[1;33m{}\033[m and \033[1;36m{}\033[m'.format(a, b))

#or

name = 'Filipe'

print('Pleasure to meet you {}{}{}'.format('\033[4;31m',name,'\033[m'))

#or
cores={'redBold':'\033[1;31m',
       'clean':'\033[m',
       'blackandwhite':'\033[1;0;40m',
       }

print('teste {a}')