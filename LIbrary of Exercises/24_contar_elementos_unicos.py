# 24 contar elementos unicos
# ===============================================
# Exercício 24: Contar Elementos Únicos numa Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que conta o número de elementos únicos numa lista.
#
# Exemplo:
# Input: [1, 2, 2, 3, 4, 4]
# Output: 4
#
# ===============================================

def contar_unicos(lista):
    return len(set(lista))


if __name__ == "__main__":
    print("=== Contar Elementos Únicos ===")
    try:
        lista = list(map(int, input("Insira os elementos da lista separados por espaço: ").split()))
        unicos = contar_unicos(lista)
        print(f"Número de elementos únicos: {unicos}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir apenas números.")
