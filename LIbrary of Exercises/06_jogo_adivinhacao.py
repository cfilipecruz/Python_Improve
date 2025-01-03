# 06 jogo adivinhacao
# ===============================================
# Exercício 6: Jogo de Adivinhação
# ===============================================
#
# Proposta do Exercício:
# Escreve um programa onde o utilizador tenta adivinhar um número aleatório
# gerado pelo computador entre 1 e 100.
#
# Exemplo:
# O computador gera o número 42.
# O utilizador tenta: 50 (muito alto), 30 (muito baixo), 42 (acertou!).
#
# ===============================================

import random


def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    print("=== Jogo de Adivinhação ===")
    print("Tente adivinhar o número entre 1 e 100!")

    while True:
        try:
            palpite = int(input("Insira o seu palpite: "))
            tentativas += 1
            if palpite < numero_aleatorio:
                print("Muito baixo!")
            elif palpite > numero_aleatorio:
                print("Muito alto!")
            else:
                print(f"Parabéns! Acertou o número {numero_aleatorio} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


if __name__ == "__main__":
    jogo_adivinhacao()
