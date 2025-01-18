# 21 gerar primos
# ===============================================
# Exercício 21: Gerar Números Primos num Intervalo
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que gera todos os números primos entre dois valores a (inclusivo) e b (inclusivo).
#
# Exemplo:
# Input: a=10, b=20
# Output: [11, 13, 17, 19]
#
# ===============================================

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gerar_primos(a, b):
    return [n for n in range(a, b + 1) if eh_primo(n)]


if __name__ == "__main__":
    print("=== Gerar Números Primos ===")
    try:
        a = int(input("Insira o valor inicial (a): "))
        b = int(input("Insira o valor final (b): "))
        if a > b:
            print("O valor inicial deve ser menor ou igual ao valor final.")
        else:
            primos = gerar_primos(a, b)
            print(f"Números primos entre {a} e {b}: {primos}")
    except ValueError:
        print("Entrada inválida. Insira números inteiros.")
