def soma(a, b):
    return a + b


def addLine(info):
    print('-'* 30)
    print(info)
    print('-'* 30)


def counter(*num):
    total = 0
    for c in num:
        total = total + c
    return total


#main
addLine('I am beautiful')
addLine('I am not beautiful')
print(soma(1, 2))
print(soma(a=5, b=2))
print(soma(b=5, a=2))

print(counter(1,2,3,4,5))
print(counter(1,2,3,4,5,293, 463, 12))

lista = [1 ,2,3,4]
print(lista * 2)
