# 32 calcular area volume geometrico
# ===============================================
# Exercício 32: Gerar Quadrado Mágico
# ===============================================
#
# Proposta do Exercício:
# Um quadrado mágico é uma matriz onde a soma de todas as linhas, colunas
# e diagonais é a mesma.
# Escreve uma função que gera um quadrado mágico de ordem ímpar.
#
# Exemplo:
# Input: 3
# Output: [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
#
# ===============================================

def gerar_quadrado_magico(n):
    if n % 2 == 0:
        raise ValueError("O tamanho deve ser ímpar.")
    quadrado = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        quadrado[i][j] = num
        i, j = (i - 1) % n, (j + 1) % n
        if quadrado[i][j] != 0:
            i = (i + 2) % n
            j = (j - 1) % n
    return quadrado


if __name__ == "__main__":
    print("=== Gerar Quadrado Mágico ===")
    try:
        n = int(input("Insira o tamanho do quadrado mágico (ímpar): "))
        if n % 2 == 0 or n <= 0:
            print("O tamanho deve ser um número ímpar maior que 0.")
        else:
            quadrado = gerar_quadrado_magico(n)
            print("Quadrado Mágico:")
            for linha in quadrado:
                print(linha)
    except ValueError as e:
        print(f"Erro: {e}")
