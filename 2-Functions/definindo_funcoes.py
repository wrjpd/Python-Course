"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

Funções que já existem, como o print, é chamada de 'função integrada(Built-int)'

Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    blodo_da_funcao

Onde:
    nome_da_funcao -> Sempre , com letras minusculas, e se for nome completo usar underline(Snake Case)
    parametros_de_entrada -> Opcionais
    bloco_da_funcao -> Corpo da função, pode ter ou não retorno da função



"""

# Exemplo 1


def diz_oi():
    print('oi')


# diz_oi()

# Em Python, podemos criar variáveis do tipo de uma função e executar esta função através da variável
oi = diz_oi
oi()
