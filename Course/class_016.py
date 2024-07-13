menu = ('Burguer', 'Soda', 'Fries', 'Desert')

for count, c in enumerate(menu):
    print(c, count)

for c in enumerate(menu):
    print(c)

for c in range(0, len(menu)):
    print(menu[c], c)

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
c = a + b
print(c)