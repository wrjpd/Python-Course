"""
Manipulando Date e Hora

Python tem um módulo built-in para se trabalhar com data e hora chamado datetime

dir(datetime) --> ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

evento=datetime.datetime.now() # Hora atual
dir(evento) --> ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']

"""

import datetime

print(datetime.MAXYEAR)  # 9999
print(datetime.MINYEAR)  # 1
print(datetime.datetime)  # class datetime


###### Classe datetime ######

# Retorna a data e hora atual yyy-mm-dd hh:mm:ss.ms
print(datetime.datetime.now())

# Qual a representação?
print(repr(datetime.datetime.now()))


###### Ajustes na data/hora ######

inicio = datetime.datetime.now()
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)


###### Criar uma data hora ######

evento = datetime.datetime(2019, 1, 1, 0)
print(evento)

# Receber data(string) e transformar em uma data
# nascimento = input("Informe sua data de nascimento (dd/mm/yyy):")
nascimento = "23/05/1998"
nascimento = nascimento.split("/")
print(datetime.datetime(int(nascimento[2]), int(
    nascimento[1]), int(nascimento[0])))


###### Acessando individualmente os elementos de data e hora ######

evento = datetime.datetime.now()
print(evento)
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)
