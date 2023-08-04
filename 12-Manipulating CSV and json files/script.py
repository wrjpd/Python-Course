"""
Lendo arquivos CSV

CSV - Comma Separeted Values

Mas podemos ter outros separadores: ; , espaço

A linguagem Python possui duas formas diferentes para ler dados em arquivo CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

"""

# Podemos ler um arquivo csv assim como qualquer outro arquivo Python


# Possível de se trabalhar, mas não é o ideal
with open('lutadores.csv',encoding='utf8') as arquivo:
    dados=arquivo.read()
    print(type(dados))
    print(dados)



# Reader
print('--')
from csv import reader

with open("lutadores.csv",encoding="utf8") as arquivo:
    leitor_csv=reader(arquivo,delimiter=',')#padrão é vírgula # devolve iterator
    next(leitor_csv) # Pula o cabeçalho    
    for linha in leitor_csv: 
        # Cada linha é uma lista
        print(f"{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centimetros")


# DictReader
print('--')
from csv import DictReader

with open('lutadores.csv',encoding='utf8') as arquivo:
    leitor_csv=DictReader(arquivo,delimiter=',')    #padrão é vírgula 
    # O cabeçalho vira as chaves do dicionário
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")
    



"""
Escrevendo em arquivos CSV

# Trabalham com listas
reader() (leitor) 
writer() (escritor)
writerrow() - Escreve uma linha

# Trabalham com dicionários
DictReader() (leitor)
DictWriter() (escritor)


"""
print('---')
from csv import writer

#writer() gera um objeto para que possamos escrever em um arquivo CSV. 
# Utilizamos o método writerow() para escrever cada linha. Este método recebe uma lista.
with open('filmes.csv','w',encoding='utf8') as arquivo:
    escritor_csv=writer(arquivo,lineterminator='\n')
    filme = None
    escritor_csv.writerow(['Título','Gênero','Duração'])    
    filme ='sair' # Comentar essa linha para testar esse bloco
    while filme != 'sair':
        filme=input("Nome do filme:")
        if filme != 'sair':
            genero=input("Informe o gênero do filme: ")
            duracao=input("Informe a duração do filme em minutos: ")
            escritor_csv.writerow([filme,genero,duracao])



print('--')
from csv import DictWriter

# Ao contrário do write() que escreve o cabeçalho e as linhas utilizando um único método. 
# O DicWriter() utiliza o método writeheader() para escrever o cabeçalho e o método writerow() para escrever as linhas.
with open('filmes2.csv','w',encoding='utf8') as arquivo:
    cabecalho=['Título','Gênero','Duração']
    escritor_csv = DictWriter(arquivo,fieldnames=cabecalho,lineterminator='\n')
    escritor_csv.writeheader() #Escreve o cabecalho no arquivo
    filme= None
    filme ='sair' # Comentar essa linha para testar esse bloco
    while filme != 'sair':
        filme=input("Nome do filme:")
        if filme != 'sair':
            genero=input("Informe o gênero do filme: ")
            duracao=input("Informe a duração do filme em minutos: ")
            escritor_csv.writerow({
                "Título":filme,
                "Gênero":genero,
                "Duração":duracao
            })



"""
Pickle

A função do Pickle é realizar o seguinte processo:
    Objeto Python -> Binarização
    Binarização -> Objeto Python

Esse processo é chamado de serialização/desserialização

# OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com arquivos pickle vidnos de outras pessoas que você não conheça ou de fontes desconhecidas.

"""
print('--')
import pickle

class Animal:

    def __init__(self,nome):
        self.__nome=nome

    def comer(self):
        print(f"{self.__nome} está comendo")

class Gato(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self._Animal__nome} está miando")

class Cachorro(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def late(self):
        print(f"{self._Animal__nome} está latindo")

felix=Gato('Felix')
pluto=Cachorro('Pluto')

# wb -> write binary
with open('animais.pickle','wb') as arquivo:
    pickle.dump((felix,pluto),arquivo)


# Fazendo a leitura de dados com arquivos pickle

with open('animais.pickle','rb') as arquivo:
    gato,cachorro=pickle.load(arquivo)
    print(gato)
    print(gato.__dict__)
    print(gato._Animal__nome)
    print(cachorro)
    print(cachorro.__dict__)
    print(cachorro._Animal__nome)



"""
Trabalhando com JSON e Pickle

JSON - JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube) e terceiros (desenvolvidos).


"""

print('--')

import json

# dumps formata para o formato json o argumento passado
ret = json.dumps(['produto',{'PlayStations 4':('2TB','Novo','220V',2340)}])
print(type(ret))
print(ret)

class Gato:

    def __init__(self,nome,raca):
        self.__nome=nome
        self.__raca=raca

    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    

felix = Gato("felix","vira-lata")

print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)


# Integrando JSON com o Pickle

import jsonpickle

# Objeto -> Arquivo
ret = jsonpickle.encode(felix)
print(ret) # {"py/object": "__main__.Gato", "_Gato__nome": "felix", "_Gato__raca": "vira-lata"}



# Escrevendo o arquivo json/pickle

felix= Gato("felix","vira-lata")

with open('felix.json','w') as arquivo:
    ret=jsonpickle.encode(felix)
    arquivo.write(ret)



# Lendo o arquivo json/pickle

with open('felix.json','r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret.__dict__)
    print(ret.nome)