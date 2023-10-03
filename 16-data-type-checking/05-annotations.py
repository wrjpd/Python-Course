"""
Annotations nos ajudam a usar os Type Hints

# Correto
texto: str

) -> str

alinhamento: bool = True

# Incorreto
texto: str
texto: str

)->str
) ->str
)-> str

alinhamento:bool = True
alinhamento: bool= True
alinhamento: bool =True


"""

import math


def circunferencia(raio: float) -> float:
    return 2*math.pi*raio


# {'raio': <class 'float'>, 'return': <class 'float'>}
print(circunferencia.__annotations__)


###### Podemos usar em variaveis fora de funções ######

nome: str = "Geek University"

ativo: bool
ativo = True

# Annotations das variáveis globais
print(__annotations__)  # {'nome': <class 'str'>, 'ativo': <class 'bool'>}

###### Classes ######


class pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f"{self.__nome} está andando"


p = pessoa("João", 38, 70.9)
print(p.__dict__)

# A instância não tem annotations
# print(p.__annotations__)

# Os métodos tem
print(p.__init__.__annotations__)
print(p.andar.__annotations__)
