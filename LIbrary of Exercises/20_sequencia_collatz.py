# 20 sequencia collatz
# ===============================================
# Exercício 20: Sequência de Collatz
# ===============================================
#
# Proposta do Exercício:
# A sequência de Collatz começa com um número inteiro positivo n e segue estas regras:
# - Se n for par, o próximo número é n / 2.
# - Se n for ímpar, o próximo número é 3 * n + 1.
# A sequência termina quando atinge o número 1.
#
# Exemplo:
# Input: 6
# Output: [6, 3, 10, 5, 16, 8, 4, 2, 1]
#
# ===============================================

def sequencia_collatz(n):
    if n <= 0:
        raise ValueError("O número deve ser maior que 0.")
    sequencia = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequencia.append(n)
    return sequencia


if __name__ == "__main__":
    print("=== Sequência de Collatz ===")
    try:
        numero = int(input("Insira um número inteiro positivo: "))
        if numero > 0:
            resultado = sequencia_collatz(numero)
            print(f"Sequência de Collatz para {numero}: {resultado}")
        else:
            print("Por favor, insira um número maior que 0.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
