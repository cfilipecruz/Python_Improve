# 30 soma diagonais matriz
# ===============================================
# Exercício 30: Calcular a Soma das Diagonais de uma Matriz
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que calcula a soma das diagonais principal e secundária de uma matriz quadrada.
#
# Exemplo:
# Input: matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: Soma das diagonais: 30
#
# ===============================================

def soma_diagonais(matriz):
    n = len(matriz)
    diagonal_principal = sum(matriz[i][i] for i in range(n))
    diagonal_secundaria = sum(matriz[i][n - i - 1] for i in range(n))
    return diagonal_principal + diagonal_secundaria


if __name__ == "__main__":
    print("=== Soma das Diagonais da Matriz ===")
    try:
        n = int(input("Insira o tamanho da matriz quadrada (n x n): "))
        if n <= 0:
            print("O tamanho da matriz deve ser maior que 0.")
        else:
            matriz = []
            print("Insira os elementos da matriz, linha por linha:")
            for _ in range(n):
                linha = list(map(int, input().split()))
                if len(linha) != n:
                    raise ValueError("Cada linha deve ter exatamente n elementos.")
                matriz.append(linha)
            soma = soma_diagonais(matriz)
            print(f"Soma das diagonais: {soma}")
    except ValueError as e:
        print(f"Erro: {e}")
