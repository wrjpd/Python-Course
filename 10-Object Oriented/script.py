"""
# O que é Orientação a objetos?

Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza mapeamento de objetos do mundo real para modelos computacionais

- Paradgima de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação a Objetos:
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente.
- Atributo -> Características do objeto.
- Método -> Comportamento do objeto (funções).
- Construtor -> Método especial utilizado para criar objetos.
- Objeto -> Instância da classe.

 





# Classes

Em POO, classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Classes podem conter:
    - Atributos -> Representam as características dos objetos. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto.
    - Métodos -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, para definir uma classe utilizamos a palavra reservada class.

Utilizamos a palavra pass em Python quando temos um bloco de código que ainda não está implementado.

Quando nomeamos uma classe em Python, utilizamos, por convenção, o nome iniciando em maiúsculo.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos que serão mapeados para classes de entidades.








# Atributos

Atributos - Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos Dinâmicos;

----Atributos de instância----
    - São atribudos declarados dentro do método construtor.
    - Método construtor é um método especial utilizado para a construção do objeto.
    - Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público, ou seja, pode ser acessado em todo o projeto.
    - Caso queiramos demonstrar que determinado atributo deve ser  tratado como privado, ou seja,que deve ser acessado somente dentro da classe, utilizamos __ no início do seu nome.(Name Mangling)

# OBS: Isso é apenas uma convenção,ou seja, a linguagem Python não vai impedir que façamos o acesso aos atributos sinalizados como privado fora da classe.
O acesso pode ser feito caso precisamos,mas não é feito de forma comum.

O que significa atributos de instância?
Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos independentemente.


----Atributos de Classe----

    - Atributos de classe são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.
    - Não precisamos de uma instância para acessar o atributo de classe.

    
----Atributos dinâmicos----
    - Atributos dinâmicos são atributos de instância que podem ser criados em tempo de execução
    - O atributo dinâmico será exclusivo da instância que o criou.







# Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em 2 grupos.
    -- Métodos de instância;
    -- Métodos de Classe;

O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.

O métodos/funções dunder em Python são chamados de métodos mágicos.

Atenção: Por mais que possamos criar nossas próprias funções utilizando dunder(duplo underline no início e no fim) não é recomendado. O Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas internas da linguagem. Então evite ao máximo, de preferência nunca o faça.


--- Métodos de instância ---
    - Precisamos de uma instância para ter acesso a ele.

--- Métodos de classe ---
    - Não estão vinculados a nenhuma instância
    - Utilizamos um decorator para sinalizar que é um método de classe
    

Caso queiramos demonstrar que determinado método deve ser  tratado como privado, ou seja,que deve ser acessado somente dentro da classe, utilizamos __ no início do seu nome.(Name Mangling)







# Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua represetanção computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo definino na classe.






# Abstração e Encapsulamento

O grande objetivo da POO (programação orientada a objetos) é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular - A classe encapsula métodos e atributos

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário





"""

# O que é Orientação a objetos?

class Produto:
    pass

ps4=Produto()
print(ps4) # <__main__.Produto object at 0x7fc183d11df0>
print(type(ps4)) # <class '__main__.Produto'>








# Classes

# Imagine que você queira automatizar o controle das lâmpadas da sua casa

# Tipo de dado: Lampada
class Lampada:
    pass

lam=Lampada()
print(type(Lampada))








# Atributos

# Atributos de instância
# Só temos acesso dentro da classe

class Lampada:
    def __init__(self,voltagem,cor): # método construtor
        self.voltagem=voltagem
        self.cor=cor
        self.        ligada= False

class ContaCorrente:
    def __init__(self,numero,limite,saldo):
        self.numero=numero
        self.limite=limite
        self.saldo=saldo



class Usuario:
    def __init__(self,nome,email,senha):
        self.nome=nome
        self.email=email
        self.senha=senha

# Classe com atributos privados

class Acesso:

    def __init__(self,email,senha):
        self.email=email
        self.__senha=senha

user=Acesso('user@gmail.com','123456')
print(user.email) # atributo público pode ser acessado
# print(user.__senha) # AttributeError: 'Acesso' object has no attribute '__senha'

# O atributo __senha está sendo sinalizado como atributo privado. Mas ainda sim conseguimos acessar ele, mas de outra forma
print(dir(user)) # ['_Acesso__senha',...]
print(user._Acesso__senha) # Temos acesso, mas não deveríamos fazer esse acesso





# Atributos de classe

class Produto:
    imposto=1.05 #atributo de classe

    def __init__(self,nome,descricao,valor):
        self.nome=nome
        self.descricao=descricao
        self.valor=valor*Produto.imposto

p1=Produto('PlayStation 4',' Video game',2300)
p2=Produto('Xbox',' Video game',4500)

# Atributos de Instância: Cada instância (p1 e p2) tem seu próprio valor para o atributo "valor".
print(p1.valor) # 2415.0
print(p2.valor) # 4725.0

# Atributos de Classe: Valor único do atributo, tanto p1,p2 e Produto tem o mesmo valor de "imposto".
print(p1.imposto) # Acesso incorreto
print(p2.imposto) # Acesso incorreto
print(Produto.imposto) # Acesso correto


# Atributos dinâmicos

p1=Produto('PlayStation 4',' Video game',2300)
p2=Produto('Xbox',' Video game',4500)

# Criando um atributo dinâmico em tempo de execução

p2.peso="5kg" # Note que na classe Produto não existe o atributo peso
print(p2.peso)

# Deletando atributos dinâmicos
print(p2.__dict__)
print("EAE")
del p2.peso
print(p2.__dict__)







# Métodos

# Método de instância

class Produto:

    contador=0

    def __init__(self,nome,descricao,valor):
        self.__id=Produto.contador+1
        self.__nome=nome
        self.__descricao=descricao
        self.__valor=valor
        Produto.contador=self.__id


    def desconto(self,porcentagem):
        """Retorna o valor do produto com desconto"""
        return(self.__valor*(100-porcentagem)/100)
    

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self,nome,sobrenome,email,senha):
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__email=email
        self.__senha=cryp.hash(senha,rounds=200000,salt_size=16)
    
    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"
    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        return False
    

   
p1=Produto('PS4','Video Game',2300)
print(p1.desconto((20)))
print(Produto.desconto(p1,20))

user1= Usuario("Angelina","Jolie","aj@gmail.com",'1234')
user2=Usuario("Felicity","Jones","fj@gmail.com",'123')
print(user1.nome_completo())
print(user2.nome_completo())


# Método de classe

class Usuario:

    contador=0

    
    @classmethod
    def conta_usuarios(cls): #cls = classe
        print(f"Temos {cls.contador} usuários no sistema")

    # Métodos estáticos

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self,nome,sobrenome,email,senha):
        self.__id=Usuario.contador+1
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__email=email
        self.__senha=cryp.hash(senha,rounds=200000,salt_size=16)
        Usuario.contador=self.__id
        print(f"Usuário criado: {self.__gera_usuario()}")
    
    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"
    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        return False

    # Métodos privados
    
    def __gera_usuario(self):
        return self.__email.split('@')[0]

Usuario.conta_usuarios()

# Métodos privados

user= Usuario('Felicity','Jones','felicityJones@gmail.com','123')

# Métodos estáticos

print(Usuario.contador)
print(Usuario.definicao())

user= Usuario('Felicity','Jones','felicityJones@gmail.com','123')

print(user.contador)
print(user.definicao())





# Objetos

class Lampada:

    def __init__(self,cor,voltagem,luminosidade):
        self.__cor=cor
        self.__voltagem=voltagem
        self.__luminosidade=luminosidade
        self.__ligada=False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        self.__ligada=not self.__ligada

class Cliente:

    def __init__(self,nome,cpf):
        self.__nome=nome
        self.__cpf=cpf

    def diz(self):
        print(f"O cliente {self.__nome} diz oi")

class ContaCorrente:

    contador=4999

    def __init__(self,limite,saldo,cliente):
        self.__numero=ContaCorrente.contador+1
        self.__limite=limite
        self.__saldo=saldo
        self.__cliente=cliente
        ContaCorrente.contador=self.__numero

    def mostra_cliente(self):
        print(f"O cliente é {self.__cliente._Cliente__nome}")

class Usuario:

    def __init__(self,nome,sobrenome,email,senha):
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__email=email
        self.__senha=senha


# instâncias ou objetos
lamp1=Lampada('branca',110,60)

lamp1.ligar_desligar()
lamp1.ligar_desligar()

print(f"A lampada está ligada? {lamp1.checa_lampada()}")

# cc1=ContaCorrente(5000,20000)

user1=Usuario('Felicity','Jones','felicity@gmail.com',123)

cli1=Cliente('angelina Jolie','123.456.789')
cc=ContaCorrente(5000,10000,cli1)
cc.mostra_cliente()

# Acessando métodos atraves de outra classse
cc._ContaCorrente__cliente.diz()





# Abstração e Encapsulamento

class Conta:

    contador=400

    def __init__(self,titular,saldo,limite):
        self.numero=Conta.contador
        self.titular=titular
        self.__saldo=saldo
        self.limite=limite
        Conta.contador +=1

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}")

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor



conta1=Conta("Geek",150,1500)


print(conta1.numero)
print(conta1._Conta__saldo)

# Podemos alterar os atributos fora da classe

conta1.numero=42
conta1._Conta__saldo=1000
print(conta1.__dict__)


# Isso acontece pq não encapsulamos nossos dados.

# Vamos refatorar

class Conta:

    contador=400

    def __init__(self,titular,saldo,limite):
        self.__numero=Conta.contador
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        Conta.contador +=1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,conta_destino):
        #1 - Remover o valor da conta de origem
        self.__saldo -= valor

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor






