# 07 extrair vogais string
# ===============================================
# Exercício 7: Extrair Vogais de uma String
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que recebe uma string e devolve uma lista com todas as vogais
# presentes na string.
#
# Exemplo:
# Input: "Python é fantástico!"
# Output: ['o', 'é', 'a', 'á', 'i', 'o']
#
# ===============================================

def extrair_vogais(texto):
    vogais = "aeiouáéíóúâêîôûãõàèìòù"
    return [char for char in texto.lower() if char in vogais]


if __name__ == "__main__":
    print("=== Extrair Vogais ===")
    texto = input("Insira um texto: ")
    resultado = extrair_vogais(texto)
    print(f"Vogais encontradas: {resultado}")
