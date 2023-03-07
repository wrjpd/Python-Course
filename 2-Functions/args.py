"""
Entendendo o *args

-O args é um parâmetro como qualquer outro.Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterico.

Exemplo: *x
-Mas por convenção, utilizamos *args para definí-lo

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
"""


def soma_todos_numeros(num1, num2, num3):
    return num1+num2+num3


print(soma_todos_numeros(4, 6, 9))
# print(soma_todos_numeros(4, 6))  typeError
# print(soma_todos_numeros(4, 6, 9,8)) typeError

# Tendo uma função com 3 parâmetros, passando 2 parâmetros ou 4 teremos um typeError.
# Para evitar o 1°, podemos utilizar valores default
# Para evitar o 2°, utilizamos o *args

# Entendendo o args


def soma_todos_numeros_2(*args):
    print(args)
    return sum(args)


print(soma_todos_numeros_2())
print(soma_todos_numeros_2(1))
print(soma_todos_numeros_2(2, 3))
print(soma_todos_numeros_2(3, 4, 5,))
print(soma_todos_numeros_2(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5]
# print(soma_todos_numeros_2(numeros))  # Retorna erro, pois args=([1,2,3,4,5],)

# Como consertar?
# o asteristico serve para informar ao python que estamos passando uma coleção de dados. Dessa forma ele saberá que precisa desempacotar estes dados.
print(soma_todos_numeros_2(*numeros))
