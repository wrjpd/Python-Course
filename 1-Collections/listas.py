"""
--- LISTAS ---

MÉTODOS E PROPRIEDADES:

>> lista=[]
>> dir(lista)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

São representadas por []
Listas em python funcionam como vetores/matrizes(arrays) em outras linguagens, com a diferença de serem DINÂMICAS e também de podermos colocar QUALQUER tipo de dado. 

Linguagens C/JAVA: Arrays
    -Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em python: 

DINÂMICO: 
    -Não possui tamanho fixo;
    -Podemos criar a lista e simplesmente ir adicionando elementos;

QUALQUER TIPO DE DADO:
    -Não possuem tipo de dado fixo
    -Podemos colocar qualquer tipo de dado


- Métodos (extend, insert,reverse,reverse,copy,pop,clear)
- Soma, Valor Máximo, Valor Mínimo, Tamanho
- CONVERSÃO Lista <-> String 
- ITERANDO
- INDICES 
- SLICING
- DESEMPACOTANDO UMA LISTA 
- COPIANDO UMA LISTA 

"""


lista1 = [1, 99, 3, 1, 5]
lista2 = ['U', 'n', 'i', 'v', 'e', 'r', 's', 'e']
lista3 = []
lista4 = list(range(11))
lista5 = list("Universe")


###
# Podemos checar se determinado valor está na lista
###

num = 10
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

letra = 'e'
if letra in lista2:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')


##################################################################################### MÉTODOS ############################################################################################


###
# Método extend
# -Podemos adicionar vários elementos em uma lista
# lista.extend([1,2,3]) adiciona cada elemento 1,2 e 3 como elemento único
# -OBS:
# extend não aceita elemento único, só elementos iteráveis como string e listas
# Podemos usar o extend para juntar duas listas  : lista1.extend(lista2)
###

lista1.extend([1, 2, 3])
print(lista1)


###
# Método insert
# -Podemos inserir um novo elemento na lista informando a posição
# -OBS:
#  Isso não substitui o valor antigo da posição, o memso será deslocado para a direita
###

print(lista2)
lista2.insert(0, 'primeiro valor')
print(lista2)


###
# Método reverse
# Podemos inverter uma lista
###

print(lista4)
lista4.reverse()
print(lista4)


###
# Método copy
# Podemos copiar uma lista
###

lista6 = lista1.copy()
print(lista1)
print(lista6)


###
# Método pop
# -Podemos remover o último elemento de uma lista
# -OBS:
#   o pop não só remove, como retorna o último elemento
###

print(lista5)
a = lista5.pop()  # retorna o última elemento
print(a)
print(lista5)

# Podemos remover um elemento pelo índice
print(lista2)
lista2.pop(2)
print(lista2)


###
# Método clear
# -Podemos limpar a lista
###

lista1.clear()
print(lista1)


######################################################################## Soma*, Valor Máximo*, Valor Mínimo*, Tamanho ##############################################################

###
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
###

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))


############################################################################# CONVERSÃO Lista <-> String #######################################################################

# PODEMOS CONVERTER UMA STRING EM UMA LISTA

# Exemplo 1
curso1 = "Programação em Python"
exemplo1 = curso1.split()
print(exemplo1)

# Exemplo2
curso2 = "Programação,em,Python"
exemplo2 = curso2.split(',')
print(exemplo2)


# PODEMOS CONVERTER UMA LISTA EM STRING

lista7 = ['Programação', 'em', 'Python']
curso3 = ' '.join(lista7)
print(curso3)

###################################################################################### ITERANDO ##########################################################################

# Iterando sobre listas

for elemento in lista4:
    print(elemento)


##################################################################################### INDICES ################################################################################


# Em listas, fazemos o acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # indice


# Gerar indice em for
print("indice for")
cores2 = list(enumerate(cores))
print(cores2)
print(type(cores2))
for indice, elemento in enumerate(cores):
    print(indice, elemento)


# Encontrar o indice de um elemento na lista
numeros = [5, 6, 6, 7, 8, 9, 10]
print(numeros.index(6))  # retorna o indice do primeiro elemento encontrado
print(numeros.index(9))


# Podemos fazer a busca a partir de um indice
print(numeros.index(6, 2))  # busca o valor 6 a partir do indice 2

# Podemos fazer a busca a partir de um indice e até um indice final
# busca o valor 6 a partir do indice 2 até o indice 5
print(numeros.index(6, 2, 5))


###################################################################################### SLICING ###########################################################################

# lista[inicio:fim:passo]

lista = [1, 2, 3, 4]
print(lista[1:])  # iniciando no indice 1 até o final
print(lista[:3])  # retorna até o indice 2
print(lista[1:3])  # iniciando no indice 1 até o indice 2

# passo
print(lista[1::2])  # inicia no 1, vai até o final de 2 em 2
print(lista[0::2])  # inicia no 1, vai até o final de 2 em 2


################################################################################ DESEMPACOTANDO UMA LISTA #################################################################################

num1, num2, num3, num4, num5, num6 = lista
print(num1)


################################################################################## COPIANDO UMA LISTA ################################################################################

# Deep Copy - duas listas diferentes; modificações em uma não alteram a outra
listaOld = [1, 2, 3]
listaNova = listaOld.copy()
listaNova.append(4)
print(listaOld)
print(listaNova)

# Shallow Copy -  cópia via atribuição. modificações em uma alteram a outra
listaOld2 = [1, 2, 3]
listaNova2 = listaOld2
listaNova2.append(4)
print(listaOld2)
print(listaNova2)
