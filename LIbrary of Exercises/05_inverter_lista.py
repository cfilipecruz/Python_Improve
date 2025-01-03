# 05 inverter lista
# ===============================================
# Exercício 5: Inverter uma Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que recebe uma lista e devolve a lista invertida.
#
# Exemplo:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# ===============================================

def inverter_lista(lista):
    return lista[::-1]


if __name__ == "__main__":
    print("=== Inversor de Lista ===")
    try:
        lista = input("Insira os elementos da lista separados por vírgula: ").split(",")
        lista_invertida = inverter_lista(lista)
        print(f"Lista invertida: {lista_invertida}")
    except Exception as e:
        print(f"Erro: {e}")
