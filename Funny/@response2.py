sair = False
valores = []

while not sair:
    try:
        valor = input('Digite um valor (ou N para terminar): ')
        if valor in 'Nn':
            sair = True
        else:
            valores.append(valor)
    except ValueError:
        print("Por favor, insira um número válido ou 'N' para terminar.")

if valores:
    valores.sort()
    valores_pares = [v for v in valores if v % 2 == 0]
    valores_impares = [v for v in valores if v % 2 != 0]

    print(f'Lista completa ordenada: {valores}')
    print(f'A lista com apenas números pares é: {valores_pares}')
    print(f'A lista com apenas números ímpares é: {valores_impares}')
else:
    print("Nenhum valor válido foi inserido.")