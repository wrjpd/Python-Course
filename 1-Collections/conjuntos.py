"""
--- CONJUNTOS ---

>> s=set({})
>> dir(s)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


-Conjuntos em qualquer linguagem de programação, estão fazendo referência à Teoria dos Conjuntos da Matemática.
-No python, os conjuntos são chamados de Sets.

Que nem na matemática:
-Sets não possuem valores duplicados (assim como dicionários não aceitam chaves duplicadas);
-Sets não possuem valores ordenados;
-Sets não são indexados (assim como dicionários);

Sets são úteis quando precisamos armazenar elementos mas não nos importamos com a ordenação deles nem chaves e valores.
Sets são referenciados com chave{}

Diferença entre Sets e Dicionários:
    -Um Dicionário tem chave/valor;
    -Um Set tem apenas valor;


-Verificar se determinado elemento está no conjunto
-Iterando
-Dicas na utlização
-Adicionando elementos
-Removendo elementos
-Copiando um conjunto
- Métodos matemáticos (união, intersecção e diferença)
- Soma, Valor Máximo, Valor Mínimo, Tamanho

"""

# Definir Set

# Forma 1
s = set({1, 2, 3, 5, 4})
print(s)

# Forma 2 = mais comum
s = {1, 2, 3, 5, 4}


########################################################################## VERIFICAR SE DETERMINADO ELEMENTO ESTÁ NO SET ########################################################

if 3 in s:
    print("Tem")
else:
    print("Não")


#################################################################################### ITERANDO ########################################################################################

for valor in s:
    print(valor)

for indice, valor in enumerate(s):
    print(indice, valor)


########################################################################### DICAS NA UTILIZAÇÃO DE CONJUNTOS ###############################################################################

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam manualmente as cidades de onde vieram

# Nós adicionamos cada cidade em uma lista, já que em uma lista podemos adicionar novos elementos e ter repetições

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
           'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

# Agora precisamos saber quantas cidades distintas existem

cidadeSet = set(cidades)  # remove as cidades iguais
print(len(cidadeSet))


############################################################################################ ADICIONANDO ELEMENTOS#################################################################
print(s)
s.add(10)
print(s)

######################################################################################## REMOVENDO ELEMENTOS##################################################################

# Forma 1
# - Caso o valor não for encontrado, será gerado um erro
# -Nenhum valor é retornado
s.remove(2)
print(s)

# Forma 2 - Caso o valor não for encontrado, nenhum erro é gerado
s.discard(1)
print(s)


################################################################################################ COPIANDO UM SET ################################################################################

# Deep Copy - duas listas diferentes; modificações em uma não alteram a outra
setOld = {1, 2, 3}
setNew = setOld.copy()
setNew.add(4)
print(setOld)
print(setNew)

# Shallow Copy -  cópia via atribuição. modificações em uma alteram a outra
setOld2 = {1, 2, 3}
setNew2 = setOld2
setNew2.add(4)
print(setOld2)
print(setNew2)

###
# Método clear
# -Podemos limpar o conjunto
###

setOld.clear()
print(setOld)


# Métodos Matemáticos
#################################################################################

# Imagine que temos dois conjuntos: Um contendo estudante do curso de Python e um contendo estudantes do curso de JavaScript

python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
javaScript = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Precisamos gerar um conjunto união.
# Forma 1 - union
unicos1 = python.union(javaScript)
print(unicos1)

# Forma 2 - pipe |
unicos2 = python | javaScript
print(unicos2)


# Precisamos gerar um conjunto intersecção.
# Forma 1 - intersection
ambos1 = python.intersection(javaScript)
print(ambos1)

# Forma 2 - utilizando &
ambos2 = python & javaScript
print(ambos2)


# Precisamos gerar diferença entre os conjuntos

so_python = python.difference(javaScript)
print(so_python)

so_javaScript = javaScript.difference(python)
print(so_javaScript)


######################################################################## Soma*, Valor Máximo*, Valor Mínimo*, Tamanho ##############################################################

###
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
###

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
