print('=' * 30)
print('Online Store'.center(30))
print('=' * 30)
total = expensive = count = cheapestPrice =0
cheapestName = ''
while True:
    productName = str(input('Product Name: '))
    price = float(input('Price: '))
    choice = str(input('Do you wish to continue (Y/N): ')).upper().strip()[0]
    total += price
    if count == 0:
        cheapestName = productName
        cheapestPrice = price
    else:
        if price < cheapestPrice:
            cheapestName = productName
            cheapestPrice = price
    if price >= 500: expensive += 1
    if choice == 'N': break
    count += 1
print(f'The total of the purchase is {total}€')
print(f'There is {expensive} expensive product(s) costing more than 500€')
print(f'The cheapest product was {cheapestName} and costed {cheapestPrice}')