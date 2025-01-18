# 34 gerador nome aleatorio
# ===============================================
# Exercício 34: Calcular Média e Soma Recursiva de uma Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função recursiva que calcula a soma e a média de uma lista.
#
# Exemplo:
# Input: [1, 2, 3, 4]
# Output: Soma: 10, Média: 2.5
#
# ===============================================

def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

def calcular_media(lista):
    soma = soma_recursiva(lista)
    return soma / len(lista) if lista else 0


if __name__ == "__main__":
    print("=== Soma e Média Recursiva ===")
    try:
        lista = list(map(float, input("Insira os números separados por espaço: ").split()))
        soma = soma_recursiva(lista)
        media = calcular_media(lista)
        print(f"Soma: {soma}, Média: {media:.2f}")
    except ValueError:
        print("Entrada inválida. Insira números válidos.")
