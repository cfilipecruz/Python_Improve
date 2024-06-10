days = int(input('Rented days? '))
km = float(input('How many km? '))

total = (days * 60) + (km * 0.15)

print("The total cost of the rent is {}".format(total))