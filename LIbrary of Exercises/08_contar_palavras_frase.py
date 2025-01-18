# 08 contar palavras frase
# ===============================================
# Exercício 8: Contar Palavras numa Frase
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que conta o número de palavras numa frase.
#
# Exemplo:
# Input: "Python é uma linguagem incrível."
# Output: 5
#
# ===============================================

def contar_palavras(frase):
    return len(frase.split())


if __name__ == "__main__":
    print("=== Contador de Palavras ===")
    frase = input("Insira uma frase: ")
    numero_palavras = contar_palavras(frase)
    print(f"Número de palavras: {numero_palavras}")



