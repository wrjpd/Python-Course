"""
List Comprehension

- Utilizando List Comprehension, podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe: [dado for dado in iterável]
# Nós podemos adicionar estruturas condicionais lógicas às nossas listas

"""
# EXEMPLOS
# Exemplo1
numeros = [1, 2, 3, 4, 5]
res = [numero*10 for numero in numeros]
print(res)

# Exemplo2
res = [numero/2 for numero in numeros]
print(res)


# Exemplo3
def funcao(valor):
    return valor*valor


res = [funcao(numero) for numero in numeros]
print(res)


# Exemplo4
nome = 'Geek University'
print([letra.upper() for letra in nome])

# Exemplo5
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.capitalize() for amigo in amigos])

# Exemplo6
print([str(numero) for numero in [1, 2, 3, 4]])


"""
Estruturas Condicionais
"""
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# 0 em Python é False
pares = [numero for numero in numeros if not numero % 2]
# 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)


# Exemplo2
res = [numero*2 if not numero % 2 else numero/2 for numero in numeros]
print(res)
