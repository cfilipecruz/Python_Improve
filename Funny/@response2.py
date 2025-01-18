from collections import Counter

def codigo_huffman(frequencias):
    arvore = {}
    for char, freq in frequencias.items():
        arvore[char] = (freq, None, None)  # (frequência, filho_esquerdo, filho_direito)

    while len(arvore) > 1:
        no_esquerdo = min(arvore, key=lambda x: arvore[x][0])
        no_direito = min(arvore - {no_esquerdo}, key=lambda x: arvore[x][0])
        nova_frequencia = arvore[no_esquerdo][0] + arvore[no_direito][0]
        arvore[f'{no_esquerdo}_{no_direito}'] = (nova_frequencia, no_esquerdo, no_direito)
        del arvore[no_esquerdo]
        del arvore[no_direito]

    codigos = {}
    def percorrer_arvore(node, codigo_atual):
        if node in frequencias:
            codigos[node] = codigo_atual
            return

        esquerda, direita = arvore[node][1:]
        percorrer_arvore(esquerda, codigo_atual + '0')
        percorrer_arvore(direita, codigo_atual + '1')

    percorrer_arvore(list(arvore.keys())[0], '')
    return codigos, arvore

def comprimir_huffman(texto, codigos):
    return ''.join(codigos[char] for char in texto)

def descomprimir_huffman(texto_comprimido, arvore):
    char_atual = ''
    resultado = ''

    for bit in texto_comprimido:
        char_atual += bit
        node = list(arvore.keys())[0]
        while arvore[node][1] is not None and arvore[node][2] is not None:
            if bit == '0':
                node = arvore[node][1]
            else:
                node = arvore[node][2]
        if arvore[node][1] is None:
            resultado += node
            char_atual = ''

    return resultado

# Exemplo de uso
texto = "aabbbcccc"
frequencias = Counter(texto)
codigos, arvore = codigo_huffman(frequencias)
texto_comprimido = comprimir_huffman(texto, codigos)
texto_descomprimido = descomprimir_huffman(texto_comprimido, arvore)

print("Texto Original:", texto)
print("Codigos Huffman:", codigos)
print("Texto Comprimido:", texto_comprimido)
print("Texto Descomprimido:", texto_descomprimido)