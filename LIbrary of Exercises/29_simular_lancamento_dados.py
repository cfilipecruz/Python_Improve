# 29 simular lancamento dados
# ===============================================
# Exercício 29: Simular Lançamento de Dados
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que simula o lançamento de n dados e retorna os resultados.
#
# Exemplo:
# Input: n = 3
# Output: [4, 6, 1] (valores aleatórios)
#
# ===============================================

import random

def lancar_dados(n):
    return [random.randint(1, 6) for _ in range(n)]


if __name__ == "__main__":
    print("=== Simular Lançamento de Dados ===")
    try:
        n = int(input("Insira o número de dados a lançar: "))
        if n <= 0:
            print("O número de dados deve ser maior que 0.")
        else:
            resultado = lancar_dados(n)
            print(f"Resultados dos lançamentos: {resultado}")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
