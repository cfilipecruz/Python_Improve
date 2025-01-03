# 03 cifra cesar
# ===============================================
# Exercício 3: Cifra de César
# ===============================================
#
# Proposta do Exercício:
# A cifra de César é uma técnica de criptografia simples que desloca cada letra de uma
# mensagem pelo número de posições definido por uma chave.
# Escreve uma função que codifica mensagens usando a cifra de César.
#
# Exemplo:
# Input: mensagem="abc", chave=2
# Output: "cde"
#
# ===============================================

def cifra_cesar(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    for char in mensagem:
        if char.lower() in alfabeto:
            deslocamento = (alfabeto.index(char.lower()) + chave) % 26
            novo_char = alfabeto[deslocamento]
            resultado += novo_char.upper() if char.isupper() else novo_char
        else:
            resultado += char
    return resultado


if __name__ == "__main__":
    print("=== Cifra de César ===")
    mensagem = input("Insira a mensagem: ")
    try:
        chave = int(input("Insira a chave (número inteiro): "))
        mensagem_codificada = cifra_cesar(mensagem, chave)
        print(f"Mensagem codificada: {mensagem_codificada}")
    except ValueError:
        print("Entrada inválida. A chave deve ser um número inteiro.")
