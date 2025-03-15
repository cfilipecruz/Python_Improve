
teste = 6
def soma(a=0, b=0):
    global teste
    teste = 7
    print(teste)
    return a + b


def addLine(info):
    """
        THis function adds fancy lines to the code with an info inside
        ------
         info
        ------
    """
    print('-'* 30)
    print(info.center(30))
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

help(addLine) # get any help with the python functions, for example help(print)