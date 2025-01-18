# 27 rotacao lista
# ===============================================
# Exercício 27: Rotacionar uma Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que rotaciona os elementos de uma lista para a direita k vezes.
#
# Exemplo:
# Input: lista = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
#
# ===============================================

def rotacionar_lista(lista, k):
    k = k % len(lista)
    return lista[-k:] + lista[:-k]


if __name__ == "__main__":
    print("=== Rotacionar Lista ===")
    try:
        lista = list(map(int, input("Insira os elementos da lista separados por espaço: ").split()))
        k = int(input("Insira o número de rotações (k): "))
        lista_rotacionada = rotacionar_lista(lista, k)
        print(f"Lista rotacionada: {lista_rotacionada}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros.")
