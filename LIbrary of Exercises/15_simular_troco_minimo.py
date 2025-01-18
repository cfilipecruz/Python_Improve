# 15 simular troco minimo
# ===============================================
# Exercício 15: Simular Troco Mínimo
# ===============================================
#
# Proposta do Exercício:
# Escreve uma função que, dado um valor em dinheiro, calcula o menor número de notas
# e moedas necessárias para fazer o troco.
#
# Exemplo:
# Input: 123
# Output: {100: 1, 20: 1, 2: 1, 1: 1}
#
# ===============================================

def calcular_troco(valor):
    notas_moedas = [100, 50, 20, 10, 5, 2, 1]
    troco = {}
    for nota in notas_moedas:
        quantidade, valor = divmod(valor, nota)
        if quantidade > 0:
            troco[nota] = quantidade
    return troco


if __name__ == "__main__":
    print("=== Simular Troco Mínimo ===")
    try:
        valor = int(input("Insira o valor em dinheiro: "))
        troco = calcular_troco(valor)
        print(f"Troco mínimo: {troco}")
    except ValueError:
        print("Entrada inválida. Insira um valor inteiro.")
