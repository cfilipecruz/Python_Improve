# 04 verificar palindromo
# ===============================================
# Exercício 4: Verificar Palíndromo
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que verifica se uma string é um palíndromo (lê-se igual de trás
# para frente).
#
# Exemplo:
# Input: "radar"
# Output: True (é um palíndromo)
#
# ===============================================

def eh_palindromo(texto):
    texto_limpo = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto_limpo == texto_limpo[::-1]


if __name__ == "__main__":
    print("=== Verificador de Palíndromo ===")
    texto = input("Insira uma palavra ou frase: ")
    if eh_palindromo(texto):
        print(f"'{texto}' é um palíndromo.")
    else:
        print(f"'{texto}' não é um palíndromo.")
