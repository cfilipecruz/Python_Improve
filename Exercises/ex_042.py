
side_01 = int(input('Type the first side: '))
side_02 = int(input('Type the second side: '))
side_03 = int(input('Type the third side: '))
total_01_02 = side_01 + side_02
total_02_03 = side_02 + side_03
total_03_01 = side_03 + side_01

if total_01_02 > side_03 and total_02_03 > side_01 and total_03_01 > side_02:
    print('The values {}, {} and {} form a triangle.'.format(side_01, side_02, side_03))
    if side_01 == side_02 == side_03:
        print('The Triangle is equilateral')
    elif side_01 == side_02 or side_03 == side_01 or side_03 == side_02:
        print('The Triangle is isosceles')
    else:
        print('The Triangle is scalene')
else:
    print('The values {}, {} and {} don´t form a triangle'.format(side_01, side_02, side_03))