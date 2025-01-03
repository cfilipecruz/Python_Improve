# 10 calcular soma digitos numero
# ===============================================
# Exercício 10: Calcular Soma dos Dígitos de um Número
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que calcula a soma de todos os dígitos de um número.
#
# Exemplo:
# Input: 12345
# Output: 15
#
# ===============================================

def soma_digitos(numero):
    return sum(int(digito) for digito in str(numero))


if __name__ == "__main__":
    print("=== Soma dos Dígitos ===")
    try:
        numero = int(input("Insira um número inteiro: "))
        resultado = soma_digitos(numero)
        print(f"Soma dos dígitos de {numero}: {resultado}")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
