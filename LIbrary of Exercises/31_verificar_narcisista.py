# 31 verificar narcisista
# ===============================================
# Exercício 31: Gerar Números Felizes
# ===============================================
#
# Proposta do Exercício:
# Um número é feliz se ao substituir o número pela soma dos quadrados dos seus dígitos
# repetidamente, o resultado final for 1.
# Escreve uma função que verifica se um número é feliz.
#
# Exemplo:
# Input: 19
# Output: True (19 é um número feliz)
#
# ===============================================

def eh_feliz(numero):
    vistos = set()
    while numero != 1 and numero not in vistos:
        vistos.add(numero)
        numero = sum(int(digito) ** 2 for digito in str(numero))
    return numero == 1


if __name__ == "__main__":
    print("=== Verificar Número Feliz ===")
    try:
        numero = int(input("Insira um número inteiro: "))
        if eh_feliz(numero):
            print(f"{numero} é um número feliz.")
        else:
            print(f"{numero} não é um número feliz.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")

