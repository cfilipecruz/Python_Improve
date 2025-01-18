# 13 encontrar segundo maior numero
# ===============================================
# Exercício 13: Encontrar o Segundo Maior Número numa Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que encontra o segundo maior número de uma lista de inteiros.
#
# Exemplo:
# Input: [10, 20, 4, 45, 99]
# Output: 45
#
# ===============================================

def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    return lista_unica[1] if len(lista_unica) > 1 else None


if __name__ == "__main__":
    print("=== Segundo Maior Número ===")
    try:
        lista = list(map(int, input("Insira números separados por espaço: ").split()))
        resultado = segundo_maior(lista)
        if resultado is not None:
            print(f"O segundo maior número é: {resultado}")
        else:
            print("A lista deve conter pelo menos dois números distintos.")
    except ValueError:
        print("Entrada inválida. Insira apenas números inteiros.")
