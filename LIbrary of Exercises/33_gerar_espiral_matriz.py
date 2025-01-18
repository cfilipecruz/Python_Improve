# 33 gerar espiral matriz
# ===============================================
# Exercício 33: Resolver Sistema de Equações Lineares
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que resolve um sistema de equações lineares representado
# na forma de matriz usando a regra de Cramer.
#
# Exemplo:
# Input: coeficientes = [[2, 1], [1, -1]], constantes = [3, 0]
# Output: [1, 2]
#
# ===============================================

import numpy as np

def resolver_sistema(coeficientes, constantes):
    matriz = np.array(coeficientes)
    vetor = np.array(constantes)
    if np.linalg.det(matriz) == 0:
        raise ValueError("O sistema não tem solução única.")
    return np.linalg.solve(matriz, vetor).tolist()


if __name__ == "__main__":
    print("=== Resolver Sistema de Equações ===")
    try:
        n = int(input("Insira o número de variáveis (n): "))
        coeficientes = []
        constantes = []
        print("Insira os coeficientes de cada equação, linha por linha:")
        for i in range(n):
            linha = list(map(float, input(f"Equação {i+1}: ").split()))
            if len(linha) != n:
                raise ValueError("Número de coeficientes inválido.")
            coeficientes.append(linha)
        constantes = list(map(float, input("Insira os termos constantes: ").split()))
        if len(constantes) != n:
            raise ValueError("Número de constantes inválido.")
        solucao = resolver_sistema(coeficientes, constantes)
        print(f"Solução: {solucao}")
    except ValueError as e:
        print(f"Erro: {e}")
