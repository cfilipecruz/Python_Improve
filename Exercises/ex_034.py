salary = int(input("What is your current salary? €"))

if salary >= 1250:
    print("Your salary with raise is {}".format(salary*1.01))
else:
    print("Your salary with raise is {}".format(salary*1.15))