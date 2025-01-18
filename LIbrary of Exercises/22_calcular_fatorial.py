# 22 calcular fatorial
# ===============================================
# Exercício 22: Calcular o Fatorial
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que calcula o fatorial de um número inteiro não negativo.
#
# Exemplo:
# Input: 5
# Output: 120
#
# ===============================================

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * calcular_fatorial(n - 1)


if __name__ == "__main__":
    print("=== Calcular Fatorial ===")
    try:
        numero = int(input("Insira um número inteiro não negativo: "))
        if numero < 0:
            print("O número deve ser não negativo.")
        else:
            resultado = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é: {resultado}")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
