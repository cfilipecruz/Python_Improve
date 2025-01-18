#Get Area
def area(length, width):
    return length * width

#Main
print('What are the sizes of the area?')
length = float(input('Length: '))
width = float(input('Width: '))
print(f'{area(length, width)} Square meters')