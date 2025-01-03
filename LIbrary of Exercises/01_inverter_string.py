# 01 inverter string
# ===============================================
# Exercício 1: Inverter uma String
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que recebe uma string como entrada e devolve a mesma string invertida.
#
# Exemplo:
# Input: "Python"
# Output: "nohtyP"
#
# ===============================================

def inverter_string(texto):
    return texto[::-1]


if __name__ == "__main__":
    print("=== Inversor de String ===")
    texto = input("Insira uma string para inverter: ")
    resultado = inverter_string(texto)
    print(f"String invertida: {resultado}")
