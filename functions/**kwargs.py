"""
**kwargs

-O kwargs é um parâmetro como qualquer outro.Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterico.

Exemplo: **x
-Mas por convenção, utilizamos **kwargs para definí-lo

-Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados e transforma esses parâmetros extras em um dicionário.

Ordem de atribuição de parâmetros:
1° - parâmetros obrigatórios
2° - *args
3° - parâmetros default(não obrigatórios)
4° - **kwargs

"""


def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(marcos='verde', julia='amarelo',
                fernanda='azul', vanessa='branco')


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return "Você recebeu um cumprimento Pythonico Geek!!"
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek!"
    return "Não tenho certeza quem é você"


print(cumprimento_especial())
print(cumprimento_especial(geek="Python"))
print(cumprimento_especial(geek="Oi"))
print(cumprimento_especial(geek="especial"))


# Desempacotar dicionários em **kwargs
def mostra_nomes(**kwargs):

    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': "Jones"}
# print(mostra_nomes(nomes)) retorna erro
print(mostra_nomes(**nomes))
