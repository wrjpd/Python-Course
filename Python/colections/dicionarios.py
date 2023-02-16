"""
--- Dicionários ---

Em algumas linguagens de programação, dicionários Python são conhecidos por mapas

Dicionários são coleções do tipo chave/valor

>> dic={}
>> dir(dic)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 
'values']

São representados por {}

OBS: Chaves e valores são separados por ':' ; 'chave:valor'
    Tanto chave,quanto valor, podem ser de qualquer tipo de dado;
    Podemos misturar tipos de dados;


-Criação
-Métodos (clear,copy,get,update,pop)
-Checar se tem alguma chave (não valor) 
-Iterações
-Acesso às chaves
-Acesso valores
-Desempacotamento de dicionários
-Soma, Valor Máximo, Valor Mínimo, Tamanho
"""

#################################################################################################### Criação de Dicionário ##################################################################################

# Forma1
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}
print(paises)

# Forma2
paises2 = dict(br='Brasil', eua='Estados Unidos', py="Paraguai")
print(paises2)

# Forma3 - Não usual - fromkeys recebe  dois parâmetros: um iterável e um valor
outro = {}.fromkeys('a', 'b')
outro2 = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
outro3 = {}.fromkeys('abcde', 'valor')
outro4 = {}.fromkeys(range(1, 11), 'novo')
print(outro)
print(outro2)
print(outro3)
print(outro4)


############################################################################################################ MÉTODOS #######################################################################################

###
# Método clear
# -Podemos limpar o dicionário
###

d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)


###
# Método copy
# -Podemos copiar o dicionário - Deep copy
###

dOld = dict(a=1, b=2, c=3)
dNew = dOld.copy()
print(dNew)

# Outra forma de copiar o dicionário - Shallow Copy

dOld2 = dict(a=1, b=2, c=3)
dNew2 = dOld2
dNew2['newValue'] = 4
print(dOld2)
print(dNew2)


###
# Método get
# - Podemos acessaros elementos de um dicionários
# - Dicionários não são indexados
###

# Forma1 -  Acessando via chave - retorna um erro caso não encontra a chave
print(paises['br'])

# Forma2 -Método get - Acessando via get - Recomendada, pois retorna 'None' caso não exista a chave
print(paises.get('br'))
# Caso o dicionário 'paises' não encontre a chave 'ru', o valor será 'Não conhecido'
russia = paises.get('ru', 'Não conhecido')

print(russia)

###
# Método update
# - Podemos atualizar/adicionar elementos
###

# Forma 1
receita = {
    'jan': 100,
    'fev': 120,
    'mar': 300
}
print(type(receita))

receita['abr'] = 350
print(receita)


# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)


###
# Método pop
# -Podemos remover dados de um dicionário
###

# Forma1 -Método pop- precisamos informar a chave, retorna erro caso não encontre a chave
receita.pop('mai')


# Forma2 - menos comum

del receita['fev']

print(receita)


########################################################################################################### Checar se tem alguma chave (não valor) ##########################################################

print('br' in paises)
print('Brasil' in paises)


##################################################################################### Qualquer tipo de dado como chaves - int,float,string, boolean,lista,tupla,dicionário ##################################

localidades = {
    (39.6895, 39.2939): (39.6895, 39.2939),
    (54.1293, 56.0989): "Escritório em NY"
}
print(localidades)


############################################################################################################### Iterações ###################################################################################

receita = {
    'jan': 100,
    'fev': 120,
    'mar': 300
}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])


############################################################################################################# Acesso às chaves #############################################################################
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

############################################################################################################# Acessando os valores #########################################################################

print(receita.values())

for valor in receita.values():
    print(valor)


######################################################################### Desempacotamento de dicionários ############################################
print(receita.items())
for chave, valor in receita.items():
    print(f'{chave}:{valor}')


############### Soma *, Valor Máximo*, Valor Mínimo, Tamanho ######################################

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
