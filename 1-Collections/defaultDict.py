"""

--- Módulo Collections - Default Dict ---

dicionario = {'curso': 'Programação em Python Essencial'}
print(dicionario)
print(dicionario['outro']) --> Gera um KeyError

Default Dict -> Ao criar um dicionário, nós informamos um valor default, podendo utilizar um lambda para isso.Este valor será retornado sempre que não houver um valor definido.
Caso tentamos acessar uma chave inexistente, essa chave será criado e o valor será atribuido

"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python Essencial'
print(dicionario)
print(dicionario['outro'])  # gera a chave 'outro' com o valor default
print(dicionario)
