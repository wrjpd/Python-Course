"""
--- TUPLAS ---

>> tupla=()
>> dir(tupla)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

São representadas por ()

Tuplas são bastante parecidas com listas.
Existem duas diferenças básicas:

1-As tuplas são representadas por parênteses ()
2-As tuplas são imutáveis: Isso significa que ao se criar uma tupla, ela não muda. Toda operação em uma tupla gera uma nova tupla.


-Cuidados
-Criar tupla com range
-Desempacotamento de tuplas
- Soma, Valor Máximo, Valor Mínimo, Tamanho
-CONCATENAÇÃO DE TUPLAS
-VERIFICAR SE DETERMINADO ELEMENTO ESTÁ NA TUPLA
-Iterando
-CONTANDO OCORRÊNCIAS EM UMA TUPLA
-Dicas
-Acesso a elementos
-indices
-slicing
"""


######################################################################################### CUIDADOS ########################################################################################

# Tuplas podem ser criadas sem parênteses
tupla1 = 1, 2, 3, 4, 5
print(tupla1, type(tupla1))


# Tuplas não podem conter somente um elemento, porém podemos criar uma tupla vazia, tupla=()
tupla2 = (4)  # é um inteiro
tupla3 = (4,)  # é uma tupla
print(tupla2, type(tupla2))
print(tupla3, type(tupla3))


########################################################################################## RANGE ####################################################################################

# Podemos gerar uma tupla dinâmicamente com o range
tupla4 = tuple(range(11))
print(tupla4)

################################################################################## DESEMPACOTAMENTO DE TUPLAS ########################################################################

tupla5 = ("University", "programação")
escola, curso = tupla5
print(escola)
print(curso)


############################################################################### SOMA*, Valor Máximo, Valor Mínimo* e Tamanho ###################################################

# * Se os valores forem todos inteiros ou reais

tupla6 = (1, 2, 3, 4, 5, 6)
print(sum(tupla6))
print(max(tupla6))
print(min(tupla6))
print(len(tupla6))


################################################################################## CONCATENAÇÃO DE TUPLAS ##################################################################

tupla7 = (1, 2, 3)
tupla8 = (4, 5, 6)
tupla9 = tupla7+tupla8

########################################################################## VERIFICAR SE DETERMINADO ELEMENTO ESTÁ NA TUPLA ########################################################

print(3 in tupla7)
print(33 in tupla7)


#################################################################################### ITERANDO ########################################################################################

for n in tupla7:
    print(n)

for indice, valor in enumerate(tupla7):
    print(indice, valor)


######################################################################### CONTANDO OCORRÊNCIAS EM UMA TUPLA #######################################################################

tupla10 = ('a', 'b', 'c', 'd', 'a', 'b', 'a')
print(tupla10.count('a'))


########################################################################### DICAS NA UTILIZAÇÃO DE TUPLAS ###############################################################################

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)


##################################################################################### ACESSO A ELEMENTOS #############################################################################

print(meses[2])
print(meses[1])


########################################################################################## INDICES #############################################################################

print(meses.index('Maio'))

# Podemos fazer a busca a partir de um indice
print(meses.index('Maio', 2))  # busca o valor 6 a partir do indice 2

# Podemos fazer a busca a partir de um indice e até um indice final
# busca o valor 6 a partir do indice 2 até o indice 5
print(meses.index('Maio', 2, 5))


############################################################################################## SLICING ##############################################################################

# tupla[inicio:fim:passo]


print(meses[1:])  # iniciando no indice 1 até o final
print(meses[:3])  # retorna até o indice 2
print(meses[1:3])  # iniciando no indice 1 até o indice 2

# passo
print(meses[1::2])  # inicia no 1, vai até o final de 2 em 2
print(meses[0::2])  # inicia no 1, vai até o final de 2 em 2
