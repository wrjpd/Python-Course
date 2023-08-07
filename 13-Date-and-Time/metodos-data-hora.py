"""
Métodos de Data e Hora
https://docs.python.org/3/library/datetime.html

# Com o now() podemos especificar um timezone,que é o fuso horário, com o today, não conseguimos

# combine() - combina datas

# weekday() - Retorna um int se referindo ao dia da semana

# strftime() - Transforma o formato da data

# strptime() - Converte string em datetime

# time() - Retorna hora



"""

import functools
import timeit
from datetime import datetime, timedelta, time


agora = datetime.now()
hoje = datetime.today()

print(agora)
print(hoje)


###### Mudanças ocorrendo à meia-noite ######

# Combine
print(time(0))  # 00:00:00
print(timedelta(days=1))
manutencao = datetime.combine((datetime.now()+timedelta(days=1)), time())
print(manutencao)


###### Encontrar o dia da semana, weekday() ######
# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# 3 - Thursday
# 4 - Friday
# 5 - Saturday
# 6 - Monday

print(datetime.now())


###### Formatando datas/horas com strftime() (String Forma Time) ######

# Brasil dd/mm/yyyy hora:minuto
hoje = datetime.today()

# Algumas formatações
print(hoje.strftime("%d/%m/%Y"))
print(hoje.strftime("%d/%m/%y"))
print(hoje.strftime("%d de %B de %Y"))


###### Transformando string em datetime ######

nascimento = datetime.strptime(
    "10/04/1968", '%d/%m/%Y')  # (string,formato)
print(nascimento)


###### Trabalhando com horas ######

almoco = time(12, 30, 0)
print(almoco)


###### Marcando tempo de execução do nosso código com timeit ######

# timeit() (string a ser executada, número de vezes)

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit(
    '"-".join(map(str,range(100)))', number=10000)
print(tempo)


###### Functools ######

def teste(n):
    soma = 0
    for num in range(n*200):
        soma = soma+num**num+4
    return soma


# functools.partial(funcao,parametro) executa a funcao a ser testada
print(timeit.timeit(functools.partial(teste, 2), number=10000))
