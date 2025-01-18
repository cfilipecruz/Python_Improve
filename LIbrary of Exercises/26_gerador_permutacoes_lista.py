# 26 gerador permutacoes lista
# ===============================================
# Exercício 26: Gerar Permutações de uma Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que gera todas as permutações possíveis de uma lista.
#
# Exemplo:
# Input: [1, 2, 3]
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
#
# ===============================================

from itertools import permutations

def gerar_permutacoes(lista):
    return list(permutations(lista))


if __name__ == "__main__":
    print("=== Gerar Permutações ===")
    try:
        lista = list(map(int, input("Insira os elementos da lista separados por espaço: ").split()))
        permutacoes = gerar_permutacoes(lista)
        print(f"Permutações: {permutacoes}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros.")
