def encontrar_palavras(matriz, palavras):
    def procurar_direcoes(matriz, palavra, linha, coluna):
        direcoes = [
            (0, 1),  # Direita
            (0, -1), # Esquerda
            (1, 0),  # Para baixo
            (-1, 0), # Para cima
            (1, 1),  # Diagonal para baixo-direita
            (-1, -1),# Diagonal para cima-esquerda
            (1, -1), # Diagonal para baixo-esquerda
            (-1, 1)  # Diagonal para cima-direita
        ]
        for dr, dc in direcoes:
            posicoes = []
            for i, letra in enumerate(palavra):
                r, c = linha + i * dr, coluna + i * dc
                if not (0 <= r < len(matriz) and 0 <= c < len(matriz[0])) or matriz[r][c] != letra:
                    break
                posicoes.append((r, c))
            if len(posicoes) == len(palavra):
                return posicoes
        return None

    resultado = {}
    for palavra in palavras:
        encontrada = False
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if matriz[linha][coluna] == palavra[0]:
                    posicoes = procurar_direcoes(matriz, palavra, linha, coluna)
                    if posicoes:
                        resultado[palavra] = (posicoes[0], posicoes[-1])
                        encontrada = True
                        break
            if encontrada:
                break
    return resultado

# Exemplo de teste:
matriz = [
    "jefblpepre",
    "camdcimgtc",
    "oivokprjsm",
    "pbwasqroua",
    "rixilelhrs",
    "wolcqlirpc",
    "screeaumgr",
    "alxhpburyi",
    "jalaycalmp",
    "clojurermt"
]

palavras = ["java", "python", "clojure", "ruby", "scala", "haskell", "perl"]

resultado = encontrar_palavras(matriz, palavras)

# Imprimir o resultado
for palavra, coords in resultado.items():
    print(f"{palavra}: {coords}")
