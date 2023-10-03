"""
Tipos em Python na prática

"""


###### Outros tipos de variáveis ######

from typing import Dict, List, Tuple, Set

nomes: list = ["Geek", "University"]
versoes: tuple = (3, 4, 7)
opcoes: dict = {"ar": True, "banco_couro": True}
valores: set = {3, 4, 5, 6}
print(__annotations__)
# {'nomes': <class 'list'>, 'versoes': <class 'tuple'>, 'opcoes': class 'dict'>, 'valores': <class 'set'>}


###### Especificar os tipos de dados internos ao containers ######

nomes2: List[str] = ["Geek", "Univesity"]
versoes2: Tuple[int, int, int] = (3, 4, 6)
dict2: Dict[str, bool] = {"ar": True, "banco_cour": True}
valores2: Set[int] = {3, 4, 5, 6}

print(__annotations__)
# 'nomes2': typing.List[str], 'versoes2': typing.Tuple[int, int, int], 'dict2': typing.Dict[str, bool], 'valores2': typing.Set[int]}
