"""
*Utilizando Lambdas*

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.
Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também.
Assim como em funções, o número errado de argumentos retornará um TypeError.

lambda x1,x2,...xn : <retorno>


*Map*

map()->Mapeia cada elemento de uma coleção e aplica uma função
Map é uma função
map(<funcao a ser executada>,colecao)


*Filter*
filter() -> Filtrar dados de uma determinada coleção


*Reduce*
Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável
reduce(funcao,dados)

A partir do Python3, a função reduce() não é mais uma função integrada(built-in). Agora temos que importar a partir do módulo 'functools'.

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes um loop for é mais legível.

Para entender o reduce(): 
# Imagine que você tem uma coleçãode dados -> dados=[a1,a2,a3,...,an]

# E você tem uma função que recebe dois parâmetros:
def funcao(x,y):
    return x*y

A função reduce(), funciona da seguinte forma:
    Passo1: res1 = f(a1,a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo2: res2 = f(res1,a3) # Aplica a função no resultado anterior e no próximo elemento da coleção e guarda o resultado
    ...

    no final, reduce() irá retornar o resultado final.




*Any e All*

all() -> Retorna True se todos os elementos do iterável são verdadeiros. Se o iterável estiver vazio retorna True

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna False






*Generators*
Em aulas anteriores nós estudamos:
-List Comprehension
-Dictionary Comprehension
-Set Comprehension

Não vimos:
-Tuple Comprehension

Não vimos, porque elas se chamam "Generators"



*Sorted*
Apesar do nome, não confundir com sort().
sort() só funciona em listas.

sorted() pode ser utilizado em qualquer iterável.
sorted() serve para ordenar elementos.
sorted() sempre retorna uma lista com os elementos do iterável ordenados.




*Min e Max*
max() -> Retorna o maior em um iterável ou o maior de dois ou mais elementos.
min() -> Retorna o menor em um iterável ou o menor de dois ou mais elementos.




*Reversed*
Não confundir com a função reverse() das listas.
reverse() só funciona com listas

reversed() funciona com qualquer iterável
reversed() reverte o iterável
reversed() retorna um iterável: list_reverseiterator



*Len,Abs,Sum e Round*

len() -> Retorna o número de itens de um iterável.
abs() -> Retorna o valor absoluto de um número real
sum() -> Retorna a soma dos elementos de um iterável, podendo receber um valor inicial.
round() -> Retorna o número passado arredondado para n digitos de precisão. Se a precisão não for passada, retorna um inteiro. 




*Zip*

zip() -> Cria um iterável (Zip Object) que agrega elementos ,em tuplas, de cada um dos iteráveis passados como entrada em pares.




"""
from os import system

#Utilizando Lambda
# Vamos criar uma função em Python
def funcao(x):
    return x+1
# Expressao Lambda
calc=lambda x:x+1
print(calc(1))

# Podemos ter expressões lambdas com múltiplas entradas
calc=lambda x,y:x+y
print(calc(1,3))
nome_completo=lambda nome,sobrenome:nome.strip().title()+' '+sobrenome.strip().title() # strip() retira os espaços em branco no começo e no final da string
print(nome_completo('joao','pedro'))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também.
texto= lambda:"Texto"
print(texto())

# Outro exemplo: Ordenar a lista pelo sobrenome
autores=['Isaac Asimov','Ray Bradbury','Robert Heinlen','Arthur C. Clarke','Frank Hertz','H. G. Wells', 'Orson Scott Card']
autores.sort(key=lambda sobrenome: sobrenome.split()[-1])
print(autores)

#Funcão quadrática
# f(x) = a*x**2+b*x+c
def geradora_funcao_quadratica(a,b,c):
    #retorna uma função em termos de x
    return lambda x:a*x**2+b*x+c

f=geradora_funcao_quadratica(1,2,3)
print(f(1))
print(f(2))
print(f(3))





#Map
#Exemplo 1: Calcular a área de um círculo
import math
def area(r):
    return math.pi*(r**2)

#E se tivermos uma coleção com raios?
raios=[2,5,7,3,10,44]
areas=map(area,raios) # Map é uma função que recebe a funcao e o iterável
print(list(areas))
print(tuple(areas))# retorna (), pois após a primeira utilização do resultado(map object), o conteudo é zerado.

# Exemplo 2: Map com lambda
print(list(map(lambda r: math.pi*r**2,raios)))

# Exemplo 3
cidades=[('Berlim',29),('Cairo',36),('Buenos Aires',19),('Los Angeles',26)]
# Celsius para Fahreint
# f=9/5*c+32
c_para_f=lambda dado: (dado[0],9/5*dado[1]+32)
fahreint=list(map(c_para_f,cidades))
print(fahreint)




# Filter
# Queremos filtrar os dados acima da média
import statistics as st # Biblioteca para trabalhar com dados estatísticos
dados=[1.3,2.7,0.8,4.1,4.3,-0.1]
print(st.mean(dados))

# Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável
res=filter(lambda x:x>st.mean(dados),dados)
print(list(res)) 
print(list(res)) # Assim como em map(), o valor some após ser utilizado pela primeira vez.

# Remover dados faltantes
paises=['','Argentina','','Brasil']
res=filter(None,paises)
print(list(res))

# Exemplo mais completo
usuarios=[
    {"username":"samuel","tweets":['Eu adoro bolos','Eu adoro pizzas']},
    {"username":"carla","tweets":['Eu adoro meu gato']},
    {"username":"jeff","tweets":[]},
    {"username":"bob123","tweets":[]},
    {"username":"doggo","tweets":['Eu gosto de cachorros','Vou sair hoje']},
    {"username":"gal","tweets":[]}
]
# Filtrar os usuários sem tweet
f=lambda x:len(x.get('tweets')) == 0
print(list(filter(f,usuarios)))

nomes=list(map(lambda x:x.get('username'),filter(f,usuarios)))
print(nomes)

# Outro exemplo
nomes=['Vanessa','Ana','Maria']
# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
f_filter=lambda x:len(x)<=5
f_map=lambda x:'Sua instrutora é '+ x

answer=list(map(f_map,filter(f_filter,nomes)))
print(answer)


# Reduce

# Exemplo, multiplicar todos os números de uma lista
from functools import reduce
dados=[2,3,4,5,7,11,13,17,19,23,29]
res=reduce(lambda x,y:x*y,dados)
print(res)

# Utilizando o for
res=1
for n in dados:
    res=res*n
print(res)




# Any e All

# All
print([i for i in range(5)])
print(all([0,1,2,3,4])) # Retorna falso, pq 0 = False
print(all([1,2,3,4]))

#Exemplo
nomes=['Carlos','Camila','Carla','Cassiano','Cristina']
print([nome[0] == 'C' for nome in nomes]) # gera uma lista cheio de 'True'
print(all([nome[0] == 'C' for nome in nomes]))# Retorna True

# Any
print(any([0,1,2,3,4]))

# Exemplo
nomes=['Carlos','Camila','Carla','Cassiano','Cristina','Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))



# Generators
# Usa menos memória do que list,dicionary, etc...
nomes=['Carlos','Camila','Carla','Cassiano','Cristina','Vanessa']
print(any(nome[0] == 'C' for nome in nomes)) # Sem o colchete []

# List Comprehesion
res =  [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res =  (nome[0] == 'C' for nome in nomes)
print(type(res))

# Podemos iterar no Generator
for i in res:
    print(i)

# getsizeof -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro.
from sys import getsizeof
print(getsizeof([nome[0] == 'C' for nome in nomes]))
print(getsizeof(nome[0] == 'C' for nome in nomes))




# Sorted
lista=[4,7,2,8,1,21]
lista.sort()
print(lista)

tupla=(4,7,2,8,1,21)
# tupla.sort() #AttributeError

tupla=(4,7,2,8,1,21)
conjunto={4,7,2,8,1,21}
print(sorted(tupla)) # retorna uma lista ordenada
print(sorted(conjunto)) # retorna uma lista ordenada

# Adicionando parâmetros ao sorted()
numeros=[6,1,8,2]
print(sorted(numeros,reverse=True)) # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas.
usuarios=[
    {"username":"samuel","tweets":['Eu adoro bolos','Eu adoro pizzas']},
    {"username":"carla","tweets":['Eu adoro meu gato']},
    {"username":"jeff","tweets":[]},
    {"username":"bob123","tweets":[]},
    {"username":"doggo","tweets":['Eu gosto de cachorros','Vou sair hoje']},
    {"username":"gal","tweets":[]}
]
# print(sorted(usuarios)) # TypeError
# Para dicionários, precisamos passar a key que queremos fazer a ordenação.
print(sorted(usuarios,key=len))
print(sorted(usuarios,key=lambda usuario:usuario["username"]))
print(sorted(usuarios,key=lambda usuario: len(usuario['tweets'])))



# system('cls')
# Min e Max
lista=[1,8,4,99,34,129]
print(max(lista))
print(min(lista))

tupla=(1,8,4,99,34,129)
print(max(tupla))
print(min(tupla))

tupla=(1,8,4,99,34,129)
print(max(tupla))
print(min(tupla))

conjunto={1,8,4,99,34,129}
print(max(conjunto))
print(min(conjunto))

dicionario={'a':1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario.values()))
print(min(dicionario.values()))


# Podemos colocar valores:
print(max(1,2,3,20))
print(min(1,2,3,20))

print(max('a','ab','abc'))
print(min('a','ab','abc'))

print(max('a','b','c','g'))
print(min('a','b','c','g'))

print(max('Geek university'))
print(min('Geek university'))

# Outros exemplos
nomes=['Arya','Samson','Dora','Tim','Ollivander']
print(max(nomes)) # Tim, 'T' vem por último
print(min(nomes)) # Arya , 'a' vem primeiro

# Mas podemos utilizar uma função
print(max(nomes,key= lambda x: len(x))) # Ollivander
print(min(nomes,key= lambda x: len(x)))

# Outro exemplo
musicas=[
    {"titulo":"Thunderstruck","tocou":3},
    {"titulo":"Dead Skin Mask","tocou":2},
    {"titulo":"Back in black","tocou":4},
    {"titulo":"Too old to rock in roll","tocou":32}
]
print(max(musicas,key=lambda musica: musica['tocou']))
print(min(musicas,key=lambda musica: musica['tocou']))




#Reversed
lista=[1,2,3,4,5]
res=reversed(lista)
print(type(res))

# podemos converter o elemento retornado para uma lista, tupla ou conjunto
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista))) # não da pra definir ordem em conjunto

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra,end="")

# Podemos utilizar o reversde() para fazer um loop reverso
for n in reversed(range(0,10)):
    print(n)




system('cls')
# Len, Abs, Sum e Round

print(len([1,2,3,4]))
print(len((1,2,3,4)))
print(len({1,2,3,4}))
print(len({'a':1,'b':2,'c':3,'d':4}))

# Por debaixo dos panos, ao utilizar a função len() o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())


print(abs(-5))
print(abs(-3.14))


print(sum([1,2,3,4]))
print(sum([1,2,3,4],5)) # soma 5 ao resultado
print(sum({'a':1,'b':2,'c':3,'d':4}.values()))


print(round(10.2))
print(round(10.5))# Até 0.5, arredonda para cima
print(round(10.6))
print(round(1.21212131212,2))



system('cls')
# Zip

# Exemplo
lista1 = [1,2,3]
lista2 =[4,5,6]
zip1=zip(lista1,lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla ou dicionário

print(list(zip(lista1,lista2))) #[(1, 4), (2, 5), (3, 6)]
print(tuple(zip(lista1,lista2))) # ((1, 4), (2, 5), (3, 6))
print(set(zip(lista1,lista2))) # {(2, 5), (1, 4), (3, 6)}
print(dict(zip(lista1,lista2)))# {1: 4, 2: 5, 3: 6}

# O zip() utiliza como parâmetros o menor tamanho em iterável.
lista3=[7,8,9,10]
print(list(zip(lista1,lista2,lista3)))


# Podemos utilizar diferentes iteráveis com zip
tupla=1,2,3,4,5
lista=[6,7,8,9,10]
dicionario={'a':11,'b':12,'c':13,'d':14,'e':15}

print(list(zip(tupla,lista,dicionario.values())))


# Lista de tuplas
dados=[(0,1),(1,2),(2,3),(3,4),(4,5)]
print(list(zip(*dados)))
print(*dados)


# Exemplos mais complexos
prova1=[80,91,78]
prova2=[98,89,53]
alunos=['maria','pedro','carla']

print(list(zip(alunos,prova1,prova2)))
final={dado[0]:(dado[1],dado[2]) for dado in zip(alunos,prova1,prova2)}
















