"""
Funções com retorno

Em Python, quando uma função não retorna nenhum valor, o retorno é None;
Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execucação da função para outras funções.

OBS return:
    -Ela finaliza a função, ou seja, ela sai da execução da função;
    -Podemos ter, em uma função, diferentes returns;
    -Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

"""

# Exemplo 1
from definindo_funcoes import diz_oi
from random import random


def quadrado_de_7():
    return 7*7


res = quadrado_de_7()
print(res)


# Exemplo 2
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

print(diz_oi())
# Vamos criar uma função para jogar uma moeda


def joga_moeda():
    # Gera um número aleatório entre 0 e 1
    valor = random()
    if valor > 0.5:
        return "Cara"
    return "Coroa"


print(joga_moeda())
