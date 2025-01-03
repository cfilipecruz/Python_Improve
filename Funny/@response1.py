def main():
    sair = False
    valores = []
    valoresPares = []
    valoresImpares = []

    while not sair:
        try:
            valor = int(input('Digite um valor: '))
            valores.append(valor)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
            continue

        escolha = input('Deseja continuar? [S/N] ').upper().strip()
        if escolha == 'N':
            sair = True

    if not valores:
        print("Nenhum valor foi inserido.")
        return

    print(f'Lista completa: {valores}')
    valores.sort()

    for v in valores:
        if v % 2 == 0:
            valoresPares.append(v)
        else:
            valoresImpares.append(v)

    print(f'A lista com apenas números pares é: {valoresPares}')
    print(f'A lista com apenas números ímpares é: {valoresImpares}')

if __name__ == "__main__":
    main()