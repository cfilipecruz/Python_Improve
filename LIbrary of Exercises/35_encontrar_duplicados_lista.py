# 35 encontrar duplicados lista
# ===============================================
# Exercício 35: Validar Expressões com Parênteses
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que verifica se uma expressão tem parênteses balanceados.
#
# Exemplo:
# Input: "(a + b) * (c + d)"
# Output: True
#
# ===============================================

def validar_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == "(":
            pilha.append(char)
        elif char == ")":
            if not pilha:
                return False
            pilha.pop()
    return len(pilha) == 0


if __name__ == "__main__":
    print("=== Validar Parênteses ===")
    expressao = input("Insira a expressão: ")
    if validar_parenteses(expressao):
        print("Os parênteses estão balanceados.")
    else:
        print("Os parênteses não estão balanceados.")
