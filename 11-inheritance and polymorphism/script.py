"""
# Herança

POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes. 

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário
    - nome
    - sobrenome
    - cpf
    - matrícula;

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?

Sim,  a entidade "Pessoa". Ao invés de criar duas classes, Cliente e Funcionário, poderemos utilizar a herança

Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada (Pessoa) é conhecia por:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe(Funcionario e Cliente) herda de outraclasse, ela é chamada:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;


    

Sobrescrita de Métodos(Overriding) ocorre quando reescrevemos um método presente na super classe em classe filhas.





# Propriedades

POO - Propriedades

Em linguagens de programação, ao delcararmos atributos privados na Classe, costumamos criar métodos públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e setter, onde os getters retornamo valor do atributo e os setters alteram o valor do atributo.





# O método super()





# Herança Múltipla





# MRO - Method Resolution





# Polimorfismo





# Métodos Mágicos







"""

# Herança

# Jeito não recomendado

class Cliente():

    def __init__(self,nome,sobrenome,cpf,renda):
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__cpf=cpf
        self.__renda=renda
    
    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"
    

class Funcionario:
    def __init__(self,nome,sobrenome,cpf,matricula):
       self.__nome=nome
       self.__sobrenome=sobrenome
       self.__cpf=cpf
       self.__matricula=matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"
    
# Jeito recomendado

class Pessoa:
    def __init__(self,nome,sobrenome,cpf):
       self.__nome=nome
       self.__sobrenome=sobrenome
       self.__cpf=cpf      

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self,nome,sobrenome,cpf,renda):   
        super().__init__(nome,sobrenome,cpf) # Acesso a classe Pessoa, estamos acessando o método __init__ de Pessoa e criando uma instância
        # Ou (Forma não comum)
        # Pessoa.__init__(self,nome,sobrenome,cpf)
        self.__renda=renda


class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""
    def __init__(self,nome,sobrenome,cpf,matricula):       
       super().__init__(nome,sobrenome,cpf)
       self.__matricula=matricula

    # Overriding
    def nome_completo(self):
        # Mesmo assim, podemos utilizar a função da classe Pai
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'{self.__matricula} Nome: {self._Pessoa__nome}'


cliente1=Cliente("Angelina","Jolie","123",5000)
func1=Funcionario("Felicity","Jones","456",123)
print(cliente1.nome_completo())
print(func1.nome_completo())











# Propriedades

class Conta:
    
    contador=0

    def __init__(self,titular,saldo,limite):
        self.__numero= Conta.contador+1
        self.__titular =titular
        self.__saldo=saldo
        self.__limite=limite
        Conta.contador+=1

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"
    
    def depositar(self,valor):
        self.__saldo+=valor
    
    def sacar(self,valor):
        self.__saldo-=valor

    def transferir(self,valor,destino):
        self.__saldo-=valor
        destino.__saldo +=valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular    
    

    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self,limite):
        self.__limite=limite

conta1=Conta("Felicity",3000,5000)
conta2=Conta("Angelina",2000,4000)

# Como somar o saldo de todas as contas?
print(conta1.get_saldo()+conta2.get_saldo())

print(conta1.__dict__)
conta1.set_limite=1
print(conta1.__dict__)



# Utilizando propriedades






# O método super()





# Herança Múltipla





# MRO - Method Resolution





# Polimorfismo





# Métodos Mágicos






