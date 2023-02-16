"""
Funções com parâmetros padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;
-Podemos colocar qualquer valor como default, até mesmo outras funções
"""

# Função exponencial


def exponencial(numero, potencia):
    return numero ** potencia


print(exponencial(2, 3))


# Função exponencial com potencia = 2 por padrão
# Em funções Python, os parâmetros com valores default DEVEM sempre estar ao final da declaração
def exponencial_padrao(numero, potencia=2):
    return numero ** potencia


print(exponencial_padrao(2))


# Sempre evite variáveis globais
total = 0


def incrementa():
    # Retorna erro; a variável local está sendo utilizada para processamento sem ter sido inicializada
    # Precisamos corrigir assim:
    global total
    total = total+1

    return total


incrementa()

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Não é local,nem global; só está na função acima
        contador = contador+1
        return contador
    return dentro()


print(fora())
