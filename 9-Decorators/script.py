"""
# Funções de maior grandeza

High Order Functions - HOF

O que são HOF?
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.

Em Python, as funçẽs são Objetos de Primeira Classe - First Class Objects


--Nested Functions--
Em Python, podemos também ter funções dentro de funções, que são conhecidas por Nested Funtions ou também Inner Functions.









# O que são decoradores

Decorators
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de HOF
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar)






# Decoradores com diferentes assinaturas

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.







# Preservando Metadata com Wraps

Metadatas -> São dados intrínsecos em arquivos.
wraps -> São funções que envolvem elementos com diversas finalidades. 






# Forçando tipos de dados com um decorador








"""

# Funções de maior grandeza

# Exemplo - Definindo as funções
def somar(a,b):
    return a + b
def diminuir(a,b):
    return a - b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

def calcular(num1,num2,funcao):
    return funcao(num1,num2)

# Testando as funções
print(calcular(4,3,somar))
print(calcular(4,3,diminuir))

# Nested Functions
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('Eai ','Suma daqui ','Gosto muito de você '))
    return humor() + pessoa
print(cumprimento('João'))


# Retornando funções de outras funções

from random import choice
def faz_me_rir():
    def rir():
        return choice(('hahahahaha','kkkkkkkk','yayayayayaya'))
    return rir

rindo=faz_me_rir()
print(rindo())

# Nested functions(ou Inne Functions) podem acessar o escopo de funções mais externas.

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada=choice(('hahahahaha','lolololo','kkkkkkkkkk'))
        return f'{risada} {pessoa}' 
    return dando_risada

rindo=faz_me_rir_novamente('fernanda')
print(rindo())







# O que são decoradores

# Decorators sem Syntact Sugar(Sintaxe não recomendada)

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você")
        funcao()
        print('Tenha um ótimo dia')
    return sendo

def saudacao():
    print('Seja bem vindo à Geek University')

# Estamos decorando/aprimorando a função "seja_educado"
teste=seja_educado(saudacao)
teste()


# Decorators com Syntact Sugar (recomendado)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()







# Decoradores com diferentes assinaturas

# Função com mais de um argumento

def gritar(funcao):
    def aumentar(*args):
        return funcao(*args).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f"Olá, eu sou o {nome}"

@gritar
def ordenar(principal,acompanhamento): # Possui dois parâmetros
    return f"Olá, eu gostaria de {principal} acompanhado de {acompanhamento}"

print(saudacao('Felicity'))
print(ordenar('Picanha','pudim'))

# Decorators com argumentos

def verifica_primeiro_argumento(valor):
    print(f"valor {valor}")    
    def interna(funcao):
        print(f"funcao {funcao}")
        def outra(*args,**kwargs):
            print(f"args {args}")
            if args and args[0] != valor:
                return f"Valor incorreto, Primeiro argumento precisa ser {valor}"
            return funcao(*args,**kwargs)
        return outra
    return interna


@verifica_primeiro_argumento("pizza") # Valor
def comida_favorita(*args): # Função
    print(args)

comida_favorita("pizza","hamburguer") # args




# Preservando Metadata com Wraps

# Problema:
 
def ver_log(funcao):
    def logar(*args,**kwargs):
        """Eu sou uma função logar dentro de outras"""
        print(f"Você está chamando {funcao.__name__}")
        print(f"Aqui está a documentação {funcao.__doc__}")
        return funcao(*args,**kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois números"""
    return a+b

print(soma.__name__) # logar
print(soma.__doc__) # """Eu sou uma função logar dentro de outras"""

# Resolução do problema
from functools import wraps
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args,**kwargs):
        """Eu sou uma função logar dentro de outras"""
        print(f"Você está chamando {funcao.__name__}")
        print(f"Aqui está a documentação {funcao.__doc__}")
        return funcao(*args,**kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois números"""
    return a+b

print(soma.__name__) # soma
print(soma.__doc__) # """Soma dois números"""









# Forçando tipos de dados com um decorador

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args,**kwargs):
            novo_args=[]
            for (valor,tipo) in zip(args,tipos):
                novo_args.append(tipo(valor))            
            return funcao(*novo_args,**kwargs)
        return converte
    return decorador

@forca_tipo(str,int)
def repete_msg(msg,vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('oi','3')




