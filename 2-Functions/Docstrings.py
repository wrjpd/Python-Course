"""
Documentando funções com Docstrings 

-Docstrings são comentários em aspas triplas

"""
# print(help(print))

# Exemplo


def diz_oi():
    """Uma função simples que retorna a string 'Oi'"""
    return 'oi'


print(diz_oi())

# Acesso a documentação da função
print(help(diz_oi))
print(diz_oi.__doc__)

