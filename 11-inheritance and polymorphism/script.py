"""
# Herança
# Propriedades
# O método super()
# Herança Múltipla
# MRO - Method Resolution Order
# Polimorfismo
# Métodos Mágicos
"""
##

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

Sim,  a entidade "Pessoa". Ao invés de criar duas classes, Cliente e Funcionário, poderemos utilizar a herança.

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada (Pessoa) é conhecida por:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe(Funcionario e Cliente) herda de outra classe, ela é chamada:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;




Sobrescrita de Métodos(Overriding) ocorre quando reescrevemos um método presente na super classe em classe filhas. Assim somente o método da classe filha será executado.
"""
# Herança

# Jeito não recomendado


class Cliente():

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


# Jeito recomendado

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        # Acesso a classe Pessoa, estamos acessando o método __init__ de Pessoa e criando uma instância
        super().__init__(nome, sobrenome, cpf)
        # Ou (Forma não comum)
        # Pessoa.__init__(self,nome,sobrenome,cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Overriding - Sobreescreve o método nome_completo da classe Pessoa()
    def nome_completo(self):
        # Mesmo assim, podemos utilizar a função da classe Pai
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'{self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente("Angelina", "Jolie", "123", 5000)
func1 = Funcionario("Felicity", "Jones", "456", 123)

print(cliente1.__dict__)
print(func1.__dict__)

print(cliente1.nome_completo())
print(func1.nome_completo())


"""
# Propriedades

POO - Propriedades

Em linguagens de programação, ao declararmos atributos privados na Classe, costumamos criar métodos públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e setter, onde os getters retornam o valor do atributo e os setters alteram o valor do atributo.

"""

# Propriedades


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador+1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta("Felicity", 3000, 5000)
conta2 = Conta("Angelina", 2000, 4000)

# Como somar o saldo de todas as contas?

# Jeito errado não recomendado
soma = conta1._Conta__saldo+conta2._Conta__saldo

# Jeito recomendado, criar um método
soma = conta1.get_saldo()+conta2.get_saldo()


print(conta1.__dict__)
conta1.set_limite = 1
print(conta1.__dict__)


# Jeito pythonico de utilizar getter e setter
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador+1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter  # [Nome da propriedade/getter].setter
    def limite(self, novo_limite):
        self.__limite = novo_limite


print(" -- ")
conta1 = Conta("Felicity", 3000, 5000)
conta2 = Conta("Angelina", 2000, 4000)

# Utilizando o getter
soma = conta1.saldo+conta2.saldo
print(soma)

# Utilizando o setter
print(conta1.__dict__)
conta1.limite = 45677
print(conta1.__dict__)


"""
POO - O método super()

O método super() se refere à super classe.

"""

# O método super()


class Animal:  # Super classe da classe Gato

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} fala {som}")


class Gato(Animal):  # Todo gato é um animal

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)

        # Podemos acessar métodos da classe pai também
        super().faz_som('auau')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')


"""
POO - Herança Múltipla

Herança múltipla nada mais é que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

Multiderivação -> Classe Cliente e Funcionário derivam da classe Pessoa.

Não importa se a derivação é direta ou indireta. A classe que realizar a herança, herdará TODOS os atributos e métodos das classes herdadas.

"""

# Herança Múltipla

# Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):  # Herda diretamente as classes Base1 e Base2
    pass


# Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):  # Herda a classe Base2 diretamente e Base1 indiretamente
    pass


# Herda a classe Base3 diretamente e as classes Base2 e Base1 indiretamente
class Multiderivada(Base3):
    pass


# Exemplo real

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar"


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando"

    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} da terra"


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)  # Super() refere-se à classe mais externa, no caso a classe Animal


# Testando
baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

# Pinguim herda qual método "cumprimentar"? O método aquático ou terrestre?
pinguim = Pinguim("Tux")
print(pinguim.andar())
print(pinguim.nadar())
# O método que é executado é o método da primeira classe herdada.
print(pinguim.cumprimentar())


# Objeto é instância de....
print(f"pinguim é instância de Pinguim? {isinstance(pinguim,Pinguim)}")  # True
# True
print(f"pinguim é instância de Terrestre? {isinstance(pinguim,Terrestre)}")
# True
print(f"pinguim é instância de Aquatico? {isinstance(pinguim,Aquatico)}")
print(f"pinguim é instância de Animal? {isinstance(pinguim,Animal)}")  # True
print(f"pinguim é instância de object? {isinstance(pinguim,object)}")  # True
# pinguim é instância de Pinguim, Terrestre, Animal, Aquatico e object.


"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos) é a ordem de execução dos métodos (quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedade da classe __mro__;
    - Via método mro()
    - Via help()


"""


# MRO - Method Resolution


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar"


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando"

    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} da terra"


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)  # Super() refere-se à classe mais externa, no caso a classe Animal


pinguim = Pinguim("Tux")
# O método que é executado é o método da primeira classe herdada.
print(pinguim.cumprimentar())

# Podemos ver a ordem de execução:

# Via propriedade da classe __mro__;
# (<class '__main__.Pinguim'>, <class '__main__.Terrestre'>, <class '__main__.Aquatico'>, <class '__main__.Animal'>, <class 'object'>)
print(Pinguim.__mro__)


# Via método mro()
# [<class '__main__.Pinguim'>, <class '__main__.Terrestre'>, <class '__main__.Aquatico'>, <class '__main__.Animal'>, <class 'object'>]
print(Pinguim.mro())


# Via help()
# print(help(Pinguim))
            # class Pinguim(Terrestre, Aquatico)
            # |  Pinguim(nome)
            # |
            # |  Method resolution order:
            # |      Pinguim
            # |      Terrestre
            # |      Aquatico
            # |      Animal
        # |      builtins.object






# Polimorfismo


"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

"""


class Animal():

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError(
            "A classe filha precisa implementar este método")

    def comer(self):
        print(f"{self.__nome} está comendo...")


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala auau")



class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau")


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

   
pluto=Cachorro('pluto')
felix=Gato('felix')
mickey=Rato('mickey')

pluto.falar()
felix.falar()
# mickey.falar()






"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder (Double Underscore).

dunder init -> __init__

"""
# Métodos Mágicos

class Livro:

    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas

    def __repr__(self): # Representação padrão da instância
        return f"{self.titulo}"
    
    def __str__(self): # Sobreescreve o método mágico __repr__
        return f"{self.titulo} escrito por {self.autor}"

    def __len__(self):
        return self.paginas
    
    def __add__(self,outro):
        return f"{self} - {outro}"
    
    def __mul__(self,outro):
        if isinstance(outro,int):
            msg=''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return "Não posso multiplicar"
   

livro1=Livro("Python",'Geek University',400)
livro2=Livro("IA com Python","Geek University",345)

# Antes de definir o método __repr__
print(livro1) # <__main__.Livro object at 0x000001F43A31DBA0>

# Método len
# antes de definir o método len:
print(len(livro1)) #<__main__.Livro object at 0x000001F43A31DBA0>


# Somar +
# Antes de definir o método add:
print(livro1+livro2) #TypeError: unsupported operand type(s) for +: 'Livro' and 'Livro'   

# Multiplicar *
# Antes de definir o método mul:
print(livro1*3)  #TypeError: unsupported operand type(s) for *: 'Livro' and 'int'   