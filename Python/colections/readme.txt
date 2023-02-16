Listas,tuplas,dicionários e conjuntos

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








--- TUPLAS ---

MÉTODOS E PROPRIEDADES:

>> tupla=()
>> dir(tupla)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

São representadas por ()

Tuplas são bastante parecidas com listas.
Existem duas diferenças básicas:

1-As tuplas são representadas por parênteses ()
2-As tuplas são imutáveis: Isso significa que ao se criar uma tupla, ela não muda. Toda operação em uma tupla gera uma nova tupla.





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






--- CONJUNTOS ---

>> s=set({})
>> dir(s)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


-Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.
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
