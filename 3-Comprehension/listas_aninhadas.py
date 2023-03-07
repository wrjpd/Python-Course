"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    Unidimensionais (arrays/vetores)
    Multidimensionais (matrizes)

Em Python nós temos as listas
"""
# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)


# Acessando so dados
print(listas[0][1])


# Iterando com loops em umalista aninhada
for lista in listas:
    for numero in lista:
        print(numero)


print('--')
[[print(valor) for valor in lista]for lista in listas]


"""
Gerando um tabuleiro
"""

tabuleiro = [[numero for numero in range(1, 4)]for valor in range(1, 4)]
print(tabuleiro)
