def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:  # Corrigido para somar apenas números pares
            soma += num
    return soma

print(soma_pares([1, 2, 3, 4, 5, 6]))  # Deve retornar 12
print(soma_pares([10, 15, 20, 25]))    # Deve retornar 30