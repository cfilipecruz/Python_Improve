weight = float(input('Tell me your weight: '))
height = float(input('Tell me your height: '))

imc = weight / (height ** 2)

if imc< 18.5:
    print('You are below weight')
elif 18.5 <= imc< 25:
    print('You are in the right weight')
elif 25 <= imc< 30:
    print('You are above weight')
elif 30 <= imc< 40:
    print('You are obese')
else:
    print('You will die')
