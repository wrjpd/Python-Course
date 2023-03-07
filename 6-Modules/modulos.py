"""
O que são módulos? 
- Em python, módulos , nada mais são que outros arquivos Python.

# Módulo random - Possui várias funções para geração de números pseudo-aleatório.


# Módulo built-in - Módulos já "instalados" em Python.
dir(__builtin__)


# Módulos customizados

Como módulos Python nada mais são do que arquivos Python, então todos os arquivos que criamos são módulos Python prontos para serem utilizados.


# Módulos externos

Utilizamos o gerenciador de pacotes Python Pip - Python Installer Package

Todos os pacotes externos oficiais: pypi.org


# Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções e variáveis para utilizarmos.
Pacote -> É um diretório contendo uma coleção de módulos.

Nas versões 2.x do Pyhon, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
Nas versões 3.x esse arquivo não é mais obrigatório, mas ainda é utilizado.



# Dunder Main e Dunder Name

Dunder -> Double Under

Dunder Name -> __name__
Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades,etc utilizando Double Under para não gerar conflitos com os nomes desses elementos na programação.

Em python, se executarmos um arquivo Python diretamente na linha de comando, internamente o Python atribuirá à variável __name__ o valor __main__ indicando que esse arquivo é o módulo de execução principal.

"""

# Módulo random

# Listar todas as funções e propriedades de um módulo:
import random
print(dir(random))

# Existem duas formas de se utilizar um módulo ou função do módulo.

# Forma 1 - Importando todo o módulo. (Não recomendado)
# Ao realizar o import de todo o módulo, estamos importando todas as funções, atributos, classes e propriedades.
import random


# Forma 2 - Importando somente uma função do módulo. (Recomendado)

from random import random
print(random())



# uniform() -> Gera um número pseudo-aleatório entre o valores estabelecidos
from random import uniform
print(uniform(3,7)) # 7 não incluído


# randint() ->Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos
from random import randint
print(randint(1,10))



# choice() -> Retorna um valor aleatório entre um iterável.
from random import choice
jogadas=['pedra','papel','tesoura']
print(choice(jogadas))



# shuffle() -> Embaralha os dados
from random import shuffle
cartas=['K','Q','J','A','2']
shuffle(cartas)
print(cartas)





# Módulos Built-in (Módulos integrados no Python)

print(dir()) # Mostra os módulos que estão carregados


# Utilizando alias (apelidos)
import random as rdm


# Podemos importar todas as funções de um módulo utilizando o*
from random import *


# Podemos dar apelido para as funções
from random import randint as rdi
print(rdi(5,89))

# Importando mais de uma função
from random import random,randint,shuffle,choice
from random import ( # Recomendado
    random,
    randint,
    shuffle,
    choice
)




# Módulos customizados

#Importando uma função específica
from funcao import soma_impares
print(soma_impares([1,2,3,4,5,6,7,8,9]))

# Importando todas as funções do módulo
import funcao as fcp
print(fcp.soma_impares([1,2,3,4,5,6,7]))
print(fcp.lista)





# Módulos externos

# pip install colorama
# colorama é utilizado para permitir impressão de textos coloridos no terminal

from colorama import Fore, Back, Style
print(Fore.RED + ' Geek')
print(Style.RESET_ALL)




# Pacotes 

# Como utilizados nossos pacotes?
# geek é o pacote
# geek1 e geek2 são os módulos

from geek import geek1,geek2
# from geek.geek1 import funcao1

print(geek1.pi)
print(geek1.funcao1(4,6))

print(geek2.curso)

# acessando um submódulo

from geek.university import geek3,geek4

print(geek3.funcao3())
print(geek4.funcao4())




# Dunder Main e Dunder Name

# Se o arquivo dunder.py for executado diretamente, a variável "__name__" receberá o valor "__main__", caso contrário, ela receberá o nome do arquivo.

import dunder
print(dunder.funcao1())