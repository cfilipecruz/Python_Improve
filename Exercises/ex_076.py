price = ('Pencil', 2, 'Eraser', 0.75, 'NoteBook', 2, 'Book', 5)

print('=' * 30)
print(f'{"Product Prices":^30}')
print('=' * 30)
for c in range(0, len(price), 2):
    print(price[c].ljust(20, '.') + str(price[c + 1]) + '€')

print('=' * 30)