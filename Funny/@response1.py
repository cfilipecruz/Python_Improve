import heapq
from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


# Função para gerar o código de Huffman
def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook


text = "exemplo de compressão de texto"
huffman_tree = huffman_coding(text)
codes = generate_codes(huffman_tree)

print("Tabela de Códigos de Huffman:")
for char, code in codes.items():
    print(f"{char}: {code}")