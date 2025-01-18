# 18 contar ocorrencias digitos
# ===============================================
# Exercício 18: Contar Ocorrências dos Dígitos de um Número
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que conta quantas vezes cada dígito aparece num número.
#
# Exemplo:
# Input: 112233
# Output: {1: 2, 2: 2, 3: 2}
#
# ===============================================

def contar_digitos(numero):
    ocorrencias = {}
    for digito in str(numero):
        ocorrencias[int(digito)] = ocorrencias.get(int(digito), 0) + 1
    return ocorrencias


if __name__ == "__main__":
    print("=== Contar Ocorrências de Dígitos ===")
    try:
        numero = int(input("Insira um número inteiro: "))
        resultado = contar_digitos(numero)
        print(f"Ocorrências dos dígitos: {resultado}")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
