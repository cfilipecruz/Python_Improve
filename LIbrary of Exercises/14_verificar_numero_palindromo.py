# 14 verificar numero palindromo
# ===============================================
# Exercício 14: Verificar se um Número é Palíndromo
# ===============================================
#
# Proposta do Exercício:
# Um número é palíndromo se ele for igual ao seu reverso.
# Exemplo: 121 é palíndromo, mas 123 não é.
#
# Escreve uma função que verifica se um número é palíndromo.
#
# Exemplo:
# Input: 121
# Output: True (é palíndromo)
#
# ===============================================

def eh_palindromo_numero(numero):
    return str(numero) == str(numero)[::-1]


if __name__ == "__main__":
    print("=== Verificar Número Palíndromo ===")
    try:
        numero = int(input("Insira um número inteiro: "))
        if eh_palindromo_numero(numero):
            print(f"{numero} é um número palíndromo.")
        else:
            print(f"{numero} não é um número palíndromo.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
