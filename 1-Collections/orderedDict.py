"""

--- Módulo Collections - Ordered Dict ---

Ordered Dict --> Dicionário que nos garante a ordem de inserção de elementos.


"""
# Em um dicionário,a ordem de inserção dos elementos não é garantida
from collections import OrderedDict
from ast import Or

dicionario1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dicionario1 = {'b': 2, 'a': 1, 'c': 3, 'd': 4, 'e': 5}


dicionario2 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})


# A ordem importa
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})


print(odict1)
print(odict2)
print(odict1 == odict2)
print(dicionario1 == dicionario2)
