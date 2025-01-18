# 12 substituir caracteres string
# ===============================================
# Exercício 12: Substituir Caracteres numa String
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que substitui todos os caracteres de uma string por outro caractere
# fornecido pelo utilizador.
#
# Exemplo:
# Input: texto="Python", substituir="*",
# Output: "******"
#
# ===============================================

def substituir_caracteres(texto, substituto):
    return substituto * len(texto)


if __name__ == "__main__":
    print("=== Substituir Caracteres ===")
    texto = input("Insira o texto: ")
    substituto = input("Insira o caractere substituto: ")
    resultado = substituir_caracteres(texto, substituto)
    print(f"Texto após substituição: {resultado}")
