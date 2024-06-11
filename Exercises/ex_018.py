import math

angle = float(input('Angle: '))

cos = math.cos(math.radians(angle))
seno = math.sin(math.radians(angle))
tan = math.tan(math.radians(angle))

print('Seno: {:.2f}'.format(seno), 'Cos: {:.2f}'.format(cos),  'Tan: {:.2f}'.format(tan))