"""
--- Módulo Collections - Counter ---

>> lista=[1,2,1]
>> res=Counter(lista)
>> dir(res)
['__add__', '__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__le__', '__len__', '__lt__', '__missing__', '__module__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', '_keep_positive', 'clear', 'copy', 
'elements', 'fromkeys', 'get', 'items', 'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'update', 'values']

Collections -> Conhecido por High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento do iterável , e como valor a quantidade de ocorrências desse elemento.


"""

from collections import Counter

# Podemos utilizar qualquer iterável
# Exemplo1
lista = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 45, 'a', 'a']
listaCounter = Counter(lista)
print(type(listaCounter))
# Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências
print(listaCounter)

# Exemplo2
string = Counter("University python")
print(string)


# Exemplo3

texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum porttitor porta nulla ut congue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas odio nisi, ultricies ac interdum eget, tincidunt ac est. Aliquam erat volutpat. Donec pharetra fringilla ligula eget ornare. Aliquam erat volutpat. Nam vel efficitur massa, nec maximus nulla. Suspendisse eu ante quis enim laoreet suscipit. Pellentesque volutpat aliquam feugiat. Maecenas tempor rutrum ex, id posuere elit dignissim non. Sed magna sapien, commodo eu ultricies et, euismod nec magna. Mauris maximus tincidunt ante eget consectetur.
"""
palavras = texto.split()

palavrasCounter = Counter(palavras)
print(palavrasCounter)


# Encontrando as 5 palavras com mais ocorrências
print(palavrasCounter.most_common(5))
