"""
MyPY

mypy nome_do_modulo.py

Só funciona se estivermos usando Type Hints, senão, nada é retornado (sucesso);

"""


def cabecalho2(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-'*len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho2("teste", 2))

# mypy nome_do_modulo.py
# ->
# 04-type-checking-MyPy.py:16: error: Argument 2 to "cabecalho2" has incompatible type "int"; expected "bool"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)
