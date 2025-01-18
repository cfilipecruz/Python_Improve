# 28 media desvio padrao lista
# ===============================================
# Exercício 28: Calcular Média e Desvio Padrão de uma Lista
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que calcula a média e o desvio padrão de uma lista de números.
#
# Exemplo:
# Input: [10, 20, 30]
# Output: Média: 20.0, Desvio Padrão: 8.16
#
# ===============================================

import math

def calcular_media_desvio(lista):
    media = sum(lista) / len(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    desvio_padrao = math.sqrt(variancia)
    return media, desvio_padrao


if __name__ == "__main__":
    print("=== Média e Desvio Padrão ===")
    try:
        lista = list(map(float, input("Insira os números separados por espaço: ").split()))
        media, desvio_padrao = calcular_media_desvio(lista)
        print(f"Média: {media:.2f}, Desvio Padrão: {desvio_padrao:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números.")
