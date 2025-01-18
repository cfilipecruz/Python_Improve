# 25 gerador combinacoes lista
# ===============================================
# Exercício 25: Gerar Combinações de uma Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que gera todas as combinações possíveis de tamanho k
# a partir de uma lista fornecida.
#
# Exemplo:
# Input: lista = [1, 2, 3], k = 2
# Output: [(1, 2), (1, 3), (2, 3)]
#
# ===============================================

from itertools import combinations

def gerar_combinacoes(lista, k):
    return list(combinations(lista, k))


if __name__ == "__main__":
    print("=== Gerar Combinações ===")
    try:
        lista = list(map(int, input("Insira os elementos da lista separados por espaço: ").split()))
        k = int(input("Insira o tamanho das combinações (k): "))
        if k > len(lista) or k <= 0:
            print("O valor de k deve ser maior que 0 e menor ou igual ao tamanho da lista.")
        else:
            combinacoes = gerar_combinacoes(lista, k)
            print(f"Combinações de tamanho {k}: {combinacoes}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros.")
