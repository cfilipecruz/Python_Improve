# 11 verificar numero triangular
# ===============================================
# Exercício 11: Verificar se um Número é Triangular
# ===============================================
#
# Proposta do Exercício:
# Um número é triangular se for o resultado da soma de todos os números inteiros de 1 até n.
# Exemplo: 6 é triangular porque 1 + 2 + 3 = 6.
#
# Escreve uma função que verifica se um número é triangular.
#
# Exemplo:
# Input: 10
# Output: False (10 não é triangular)
#
# ===============================================

def eh_triangular(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
        if soma == numero:
            return True
        if soma > numero:
            return False


if __name__ == "__main__":
    print("=== Verificar Número Triangular ===")
    try:
        numero = int(input("Insira um número inteiro: "))
        if eh_triangular(numero):
            print(f"{numero} é um número triangular.")
        else:
            print(f"{numero} não é um número triangular.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
