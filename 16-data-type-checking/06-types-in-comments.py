"""
Podemos definir os tipos como comentários.
-> O mypy pega se houve error
-> __annotations__ não retorna nada

"""

import math


def circunferencia(raio, area=True):
    # type: (float,bool) -> float
    return 2*math.pi*raio


###### Outra forma ######

def cabecalho(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return "a"
    else:
        return "b"
