# 16 encontrar todos os divisores
# ===============================================
# Exercício 16: Encontrar Todos os Divisores de um Número
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que encontra todos os divisores de um número inteiro positivo.
#
# Exemplo:
# Input: 12
# Output: [1, 2, 3, 4, 6, 12]
#
# ===============================================

def encontrar_divisores(numero):
    return [i for i in range(1, numero + 1) if numero % i == 0]


if __name__ == "__main__":
    print("=== Encontrar Divisores ===")
    try:
        numero = int(input("Insira um número inteiro positivo: "))
        if numero > 0:
            divisores = encontrar_divisores(numero)
            print(f"Divisores de {numero}: {divisores}")
        else:
            print("Por favor, insira um número maior que 0.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
