# 09 filtrar numeros pares lista
# ===============================================
# Exercício 9: Filtrar Números Pares de uma Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que recebe uma lista de números e devolve apenas os números pares.
#
# Exemplo:
# Input: [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]
#
# ===============================================

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]


if __name__ == "__main__":
    print("=== Filtrar Números Pares ===")
    try:
        lista = list(map(int, input("Insira números separados por espaço: ").split()))
        pares = filtrar_pares(lista)
        print(f"Números pares: {pares}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir apenas números inteiros.")
