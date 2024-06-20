import time

number = 10

for c in range(0, 11):
    print(number)
    number -= 1
    time.sleep(1)

#or

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)