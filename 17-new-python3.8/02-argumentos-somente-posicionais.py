"""
dir(float) -> 
class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating point number, if possible.
 |
 |  Methods defined here:
 |
 .....


Em "float(x=0, /)", a barra "/" indica que x, e tudo que tiver antes dela, é "somente posicional", ou seja, não podemos chamar float(x=valor), mas sim float(valor).

"*" indica que todos os parâmetros depois dele devem ser informados

"""


### Exemplo ###

def cumprimenta_v1(nome):
    return f"Olá {nome}"


print(cumprimenta_v1("Geek"))  # Funcionca
print(cumprimenta_v1(nome="Geek"))  # Funciona


def cumprimenta_v2(nome, /):
    return f"Olá {nome}"


print(cumprimenta_v2("Geek"))  # Funcionca
# print(cumprimenta_v2(nome="Geek"))  # Não Funciona


### Mais de 1 argumento ###

def cumprimenta_v3(nome, /, mensagem="Olá"):
    return f"{mensagem} {nome}"


print(cumprimenta_v3("Geek"))
print(cumprimenta_v3("University", mensagem="Hello"))
print(cumprimenta_v3("Felicity", "Bem-vindo"))


def cumprimenta_v4(nome, mensagem="Olá", /):
    return f"{mensagem} {nome}"


print(cumprimenta_v4("Geek"))
# print(cumprimenta_v4("University", mensagem="Hello")) # Não funciona
print(cumprimenta_v4("Felicity", "Bem-vindo"))


### * ###

def cumprimenta_v5(*, nome):
    return "olá"


# print(cumprimenta_v5("Geek")) # Não funciona
print(cumprimenta_v5(nome="Geek"))


### Misturando tudo ###

def cumprimenta_v6(nome, /, mensagem="Olá", *, mensagem2):
    return f"{mensagem} {nome} {mensagem2}"


print(cumprimenta_v6("Geek", "teste", mensagem2="Tenha um bom dia"))
