# 19 verificar potencia de dois
# ===============================================
# Exercício 19: Verificar Potência de Dois
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que verifica se um número é uma potência de dois.
#
# Exemplo:
# Input: 16
# Output: True (16 é uma potência de 2)
#
# ===============================================

def eh_potencia_de_dois(numero):
    return numero > 0 and (numero & (numero - 1)) == 0


if __name__ == "__main__":
    print("=== Verificar Potência de Dois ===")
    try:
        numero = int(input("Insira um número inteiro: "))
        if eh_potencia_de_dois(numero):
            print(f"{numero} é uma potência de 2.")
        else:
            print(f"{numero} não é uma potência de 2.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
