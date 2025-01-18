# 23 anagramas
# ===============================================
# Exercício 23: Verificar Anagramas
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que verifica se duas palavras ou frases são anagramas.
# Um anagrama é formado rearranjando as letras de uma palavra/frase.
#
# Exemplo:
# Input: "amor", "roma"
# Output: True
#
# ===============================================

def eh_anagrama(texto1, texto2):
    texto1_limpo = sorted(texto1.replace(" ", "").lower())
    texto2_limpo = sorted(texto2.replace(" ", "").lower())
    return texto1_limpo == texto2_limpo


if __name__ == "__main__":
    print("=== Verificar Anagramas ===")
    texto1 = input("Insira a primeira palavra ou frase: ")
    texto2 = input("Insira a segunda palavra ou frase: ")
    if eh_anagrama(texto1, texto2):
        print(f"'{texto1}' e '{texto2}' são anagramas.")
    else:
        print(f"'{texto1}' e '{texto2}' não são anagramas.")
