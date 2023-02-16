"""
#Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do código.

Erros e Exceptions são sinônimos na programação.


Erros mais comuns:

-SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o python não reconhece como parte da linguagem.

-NameError -> Ocorre quando uma variável ou função não foi definida.

-TypeError -> Ocorre quando uma função/operação é aplicada a um tipo errado.

-IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido.

-ValueError -> Ocorre quando uma função/operação built-in recebe um argumento com tipo corretor mas valor inapropriado.

-KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

-AttributeError -> Ocorre quando uma variável não tem atributo/função.

-IndentationError -> Ocorre quando não respeitamos a indentação do python(4 espaços).



# Levantando os próprios erros com raise

raise -> Lança exceções
O raise não é uma função. É uma palavra reservada, assim como 'def' ou qualquer  outra em Python.
Para simplificar, pense no raise como sendo útil para que possamos criar nossas própias exceções e mensagens de erro.
O raise,assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

A foram geral de utilização é: 

raise TipoDoErro('Mensagem de erro')

"""

from os import system
# Erros mais comuns 

# # SyntaxError

# # Exemplo 1
# def funcao:
#     print('Geek University')


# # Exemplo 2
# def=1
# None =1
# return




# NameError

# # Exemplo 1
# print(geek)


# # Exemplo 2
# geek()




# TypeError

# # Exemplo 1
# print(len(3))
# print('Geek' + [])




# IndexError

# # Exemplo 1
# lista=['Geek']
# print(lista[2])




# ValueError

# # Exemplo 1
# print(int('Geek'))
# print(float('Geek'))




# KeyError

# # Exemplo 1
# dic={}
# print(dic['geek'])




# AtribbuteError

# # Exemplo 1
# tupla=(11,2,3,4)
# print(tupla.sort())




# IndentationError

# # Exemplo 1
# def nova():
# print('geek')

# # Exemplo 2
# for i in range(10):
# print(i)





# Levantando os próprios erros com raise
# raise ValueError('Mensagem de erro que eu quiser')

# Exemplo real - TypeError
def colore(texto,cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('geek','azul')
# colore('geek',4)


# Exemplo 2 - ValueError
def colore(texto,cor):
    cores_aceitas = ('verde','amarelo','azul','branco') 
    if cor not in cores_aceitas:
        raise ValueError(f'A cor precisa ser uma entre:{cores_aceitas}')
    print(f'O texto {texto} será impresso na cor {cor}')
# colore('geek','preto')









