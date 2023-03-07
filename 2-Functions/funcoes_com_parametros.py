"""
Funções com parâmetros

-Funções que recebem dados para serem processados dentro da mesma
-Já sabemos que existem funções que:
    Não posuem entrada
    Não possuem saida
    Possuem entrada mas não possuem saída
    Não possuem entrada mas possui saída
    Possuem entrada e saída
"""


def quadrado(x, y):

    return x**y


print(quadrado(7, 2))


# Diferença entre parâmetros e argumentos
# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são variáveis passados durante a execucação de uma função;


def nome_completo(nome, sobrenome):
    print(f"Seu nome completo é {nome} {sobrenome}")


nome_completo('Angelina', 'Jolie')
# Argumentos nomeados( Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos, podemos utilizar em qualquer ordem


nome_completo(sobrenome="Jolie", nome="Angelina")
