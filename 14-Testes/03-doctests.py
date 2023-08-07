"""
Doc tests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do docteste:
python -m doctest -v filename.py

# Output:
Trying:
    soma(1,2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

Obs: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.

"""


def soma(a, b):
    """
    Soma os números a e b
    #>>> soma(1,2)
    3
    #>>> soma(4,6)
    10

    """

    return a+b


###### Outro exemplo, aplicando o TDD ######

def duplicar(valores):
    """
    Duplica os valores em uma lista

    #>>> duplicar([1,2,3,4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a','b','c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True,None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    """

    return [2 * element for element in valores]


###### Erro inesperado ######

def fala_oi():
    """
    Fala oi

    #>>> fala_oi()
    "oi"

    """

    return "oi"

# Temos que trocar o "oi" do teste por 'oi' -> aspas simples por causa das aspas duplas da documentação da função


###### Erro inesperado ######

def verdade():
    """
    Retorna verdade

    >>> verdade()
    True  

    """
    return True

# Depois de "True" temos dois espaços, isso causa falha nos testes
