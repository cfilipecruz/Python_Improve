import math

catetooposto = float(input('Digite o valor do cateto oposto: '))
catetoadjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(catetooposto, catetoadjacente)

print("O valor da ipotnusa é {:.2f}".format(hipotenusa))