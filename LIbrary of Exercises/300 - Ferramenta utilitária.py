import math


class FerramentaUtilitaria:
    def __init__(self):
        self.a_correr = True

    def menu(self):
        print("\n=== Ferramenta Utilitária ===")
        print("1. Calcular Fatorial")
        print("2. Gerar Sequência de Fibonacci")
        print("3. Inverter uma String")
        print("4. Verificar Número Primo")
        print("5. Sair")

    def calcular_fatorial(self):
        try:
            numero = int(input("Insira um número para calcular o seu fatorial: "))
            if numero < 0:
                print("O fatorial não está definido para números negativos.")
            else:
                print(f"O fatorial de {numero} é {math.factorial(numero)}.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

    def gerar_fibonacci(self):
        try:
            comprimento = int(input("Insira o comprimento da sequência de Fibonacci: "))
            if comprimento <= 0:
                print("O comprimento deve ser um número inteiro positivo.")
            else:
                fib = [0, 1]
                for _ in range(2, comprimento):
                    fib.append(fib[-1] + fib[-2])
                print(f"Sequência de Fibonacci com comprimento {comprimento}: {fib[:comprimento]}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

    def inverter_string(self):
        texto = input("Insira uma string para inverter: ")
        print(f"String invertida: {texto[::-1]}")

    def verificar_primo(self):
        try:
            numero = int(input("Insira um número para verificar se é primo: "))
            if numero <= 1:
                print(f"{numero} não é um número primo.")
                return
            for i in range(2, int(math.sqrt(numero)) + 1):
                if numero % i == 0:
                    print(f"{numero} não é um número primo.")
                    return
            print(f"{numero} é um número primo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

    def executar(self):
        while self.a_correr:
            self.menu()
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                self.calcular_fatorial()
            elif escolha == "2":
                self.gerar_fibonacci()
            elif escolha == "3":
                self.inverter_string()
            elif escolha == "4":
                self.verificar_primo()
            elif escolha == "5":
                print("A sair da ferramenta. Até breve!")
                self.a_correr = False
            else:
                print("Escolha inválida. Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    ferramenta = FerramentaUtilitaria()
    ferramenta.executar()
