"""
Dictionary Comprehension

Pense no seguinte:
Se quisermos criar uma lista fazemos:
lista=[1,2,3,4]

Se quisermos criar uma tupla:
tupla=(1,2,3,4)

Se quisermos criar um set:
set={1,2,3,4}

Se quisermos criar um dicionário:
dicionario={'a':1,'b':2,'c':3,'d':4}

#list comprehension:
[valor for valorin iteravel]

#Sintaxe
{chave:valor for valor in iterável}

"""
# Exemplos
numero = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# Elevar os valores ao quadrado de um dicionário
quadrado = {chave: valor**2 for chave, valor in numero.items()}
print(quadrado)


# Exemplo2 - Iterar uma lista
numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor**2 for valor in numeros}
print(quadrados)


# Exemplo3
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)


# Um exemplo com lógica condicional - Checar a paridade dos numeros>

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if not num % 2 else 'impar') for num in numeros}
print(res)
