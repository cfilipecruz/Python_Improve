number = 0
count = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            count += 1
            number = number + c
print(count)
print(number)
