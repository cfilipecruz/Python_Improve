# 17 simular jogo de dados
# ===============================================
# Exercício 17: Simular Jogo de Dados
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que simula o lançamento de dois dados e retorna o resultado.
#
# Exemplo:
# Output: Dados: 3, 5
#
# ===============================================

import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2


if __name__ == "__main__":
    print("=== Simular Lançamento de Dados ===")
    dado1, dado2 = lancar_dados()
    print(f"Resultado: Dado 1 = {dado1}, Dado 2 = {dado2}")
