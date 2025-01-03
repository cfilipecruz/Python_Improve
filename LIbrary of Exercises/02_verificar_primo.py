# 02 verificar primo
# ===============================================
# Exercício 2: Verificar Número Primo
# ===============================================
#
# Proposta do Exercício:
# Um número primo é um número maior que 1 que só pode ser dividido por 1 e por ele mesmo.
# Escreve uma função que verifica se um número inteiro é primo.
#
# Exemplo:
# Input: 7
# Output: True (é primo)
#
# ===============================================

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("=== Verificador de Número Primo ===")
    try:
        numero = int(input("Insira um número inteiro: "))
        if eh_primo(numero):
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
