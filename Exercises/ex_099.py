def bigger (* numbers):
    bigger = 0
    for index, number in enumerate(numbers):
        if index == 0:
            bigger = number
        else:
            if number > bigger:
                bigger = number

    return f"The biggest value is {bigger}"

print(bigger(1,2,3,4,5))
print(bigger(-5, -10, -1, -20, -15))       # Output: The biggest value is -1
print(bigger(100))                         # Output: The biggest value is 100
print(bigger(0, 0, 0, 0, 0))               # Output: The biggest value is 0
print(bigger(-50, 50, -100, 0, 49))        # Output: The biggest value is 50
print(bigger(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Output: The biggest value is 10