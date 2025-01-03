import os

# Lista organizada por nível de dificuldade com nomes de ficheiros
exercicios = [
    "01_inverter_string.py",
    "02_verificar_primo.py",
    "03_cifra_cesar.py",
    "04_verificar_palindromo.py",
    "05_inverter_lista.py",
    "06_jogo_adivinhacao.py",
    "07_extrair_vogais_string.py",
    "08_contar_palavras_frase.py",
    "09_filtrar_numeros_pares_lista.py",
    "10_calcular_soma_digitos_numero.py",
    "11_verificar_numero_triangular.py",
    "12_substituir_caracteres_string.py",
    "13_encontrar_segundo_maior_numero.py",
    "14_verificar_numero_palindromo.py",
    "15_simular_troco_minimo.py",
    "16_encontrar_todos_os_divisores.py",
    "17_simular_jogo_de_dados.py",
    "18_contar_ocorrencias_digitos.py",
    "19_verificar_potencia_de_dois.py",
    "20_sequencia_collatz.py",
    "21_gerar_primos.py",
    "22_calcular_fatorial.py",
    "23_anagramas.py",
    "24_contar_elementos_unicos.py",
    "25_gerador_combinacoes_lista.py",
    "26_gerador_permutacoes_lista.py",
    "27_rotacao_lista.py",
    "28_media_desvio_padrao_lista.py",
    "29_simular_lancamento_dados.py",
    "30_soma_diagonais_matriz.py",
    "31_verificar_narcisista.py",
    "32_calcular_area_volume_geometrico.py",
    "33_gerar_espiral_matriz.py",
    "34_gerador_nome_aleatorio.py",
    "35_encontrar_duplicados_lista.py",
    "36_encontrar_elemento_mais_frequente.py",
    "37_converter_decimal_para_binario.py",
    "38_encontrar_numero_faltante_lista.py",
    "39_gerar_senha_aleatoria.py",
    "40_gerar_tabela_multiplicacao.py",
    "41_simular_baralho_cartas.py",
    "42_ordenar_lista_palavras.py",
    "43_fatorial_sem_recursao.py",
    "44_simulador_jogo_da_forca.py",
    "45_encontrar_pares_com_soma_dada.py",
    "46_gerar_matriz_identidade.py",
    "47_calcular_maior_reto_area.py",
    "48_gerar_sublistas_lista.py",
    "49_gerar_numeros_perfeitos.py",
    "50_resolver_torres_hanoi.py",
    "51_conversor_bases.py",
    "52_enigma_das_rainhas.py",
    "53_transformar_matriz_90graus.py",
    "54_ordenacao_quicksort.py",
    "55_fibonacci_com_memoizacao.py",
    "56_busca_binaria.py",
    "57_gerar_sudoku_basico.py",
    "58_soma_subconjuntos.py",
    "59_validador_parenteses.py",
    "60_compressao_run_length.py",
    "61_calcular_mdc_euclides.py",
    "62_potencia_recursiva.py",
    "63_verificar_numeros_armstrong.py",
    "64_gerar_piramide_numerica.py",
    "65_gerar_numeros_felizes.py",
    "66_gerar_quadrado_magico.py",
    "67_resolver_sistema_equacoes.py",
    "68_calculadora_notacao_polonesa.py",
    "69_simulador_fila_atendimento.py",
    "70_gerar_matriz_transposta.py",
    "71_converter_romanos_para_inteiros.py",
    "72_ordenacao_bubble_sort.py",
    "73_calcular_maior_subsequencia_soma.py",
    "74_simulador_jogo_pedra_papel_tesoura.py",
    "75_determinante_de_matriz.py",
    "76_gerar_numero_primo_aleatorio.py",
    "77_calcular_distancia_euclidiana.py",
    "78_verificar_string_balancada.py",
    "79_ordenar_lista_sem_sort.py",
    "80_encontrar_numero_mais_proximo.py",
    "81_calcular_media_harmonica.py",
    "82_calcular_menor_diferenca_lista.py",
    "83_simulador_sequencia_fibonacci.py",
    "84_resolver_expressao_infixa.py",
    "85_calcular_numero_harmonico.py",
    "86_verificar_sequencia_aritmetica.py",
    "87_encontrar_pares_ordenados_lista.py",
    "88_calcular_determinante_matriz_3x3.py",
    "89_gerar_tabuleiro_xadrez.py",
    "90_verificar_lista_circular.py",
    "91_encontrar_maior_sequencia_consecutiva.py",
    "92_resolver_equacao_quadratica.py",
    "93_calcular_media_geometrica.py",
    "94_gerar_tabela_truth_table.py",
    "95_simular_batalha_naval.py",
    "96_calcular_pi_por_monte_carlo.py",
    "97_simulador_caminho_aleatorio.py"
]


# Diretório onde os ficheiros serão criados
diretorio = os.getcwd()

# Criar o diretório se não existir
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Criar os ficheiros
for exercicio in exercicios:
    caminho_ficheiro = os.path.join(diretorio, exercicio)
    if not os.path.exists(caminho_ficheiro):
        with open(caminho_ficheiro, "w") as ficheiro:
            # Inserir um cabeçalho básico no ficheiro
            ficheiro.write(f"# {exercicio.replace('_', ' ').replace('.py', '').capitalize()}\n")
        print(f"Ficheiro criado: {caminho_ficheiro}")
    else:
        print(f"O ficheiro já existe: {caminho_ficheiro}")
