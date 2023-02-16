"""
Set Comprehension
"""

numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x**2 for x in range(10)}
print(numeros)

letra = {letra for letra in 'Geek University'}
print(letra)
