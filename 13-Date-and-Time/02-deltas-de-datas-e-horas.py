"""
Trabalhando com deltas de datas e horas

data_inicial=''
data_final=''

duração do evento = delta(data_final-data_inicial)

"""
from datetime import datetime, timedelta

# Data de hoje
data_hoje = datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime(2023, 10, 20)

# Calculando o delta
tempo_para_evento = aniversario-data_hoje
print(tempo_para_evento)
print(tempo_para_evento.days)
print(type(tempo_para_evento))  # datetime.timedelta


###### Adicionar dias para o futuro ######

data_da_compra = datetime.now()
regra_boleto = timedelta(days=3)
vencimento = data_da_compra+regra_boleto
print(vencimento)
