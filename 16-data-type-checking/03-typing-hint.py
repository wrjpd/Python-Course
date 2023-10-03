"""
Tipagem Estática com Python

# Type hints
-> Recurso que permite especificar o tipo de dado de uma variável;
-> Type Hints não tornam o Python uma linguagem estaticamente tipada;
-> São utilizadas como documentação;

"""

####### Exemplo de Type Hint ######


def cumprimentar(nome: str) -> str:
    print(type(nome))
    return f"Olá, {nome}"


print(cumprimentar(1))


###### Outro exemplo ######

def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-'*len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho("Geek University"))
print(cabecalho("Geek University", alinhamento=False))


# Utilizando Type Hint:

def cabecalho2(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-'*len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


# Isso não afeta em nada o código, só server para documentar a função e ajudar a IDE a verificar o código
# Se passarmos "alinhamento=3", não haverá problema:

print(cabecalho2("teste", 2))  # Não da erro
