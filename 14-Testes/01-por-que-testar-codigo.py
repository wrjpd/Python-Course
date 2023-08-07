"""
Por que testar nosso código?

Testes automatizados!

		Aplicação web
 --------------------------------
 /       						/
 /      frontend e backend      /
 --------------------------------
 /		testes automatizados	/
 --------------------------------

Por que testar nosso código?
	- Reduzir bugs no código existente;
	- Testes garantem que novos recursos da sua aplicação não quebrem recursos antigos;
    - Testes garantem que bugs que foram corrigidos anteriormente continuem corrigidos;
    - Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs;
 
TDD - Test Driven Development (Desenvolvimento Guiado por Testes)
Com TDD é utilizado estágios de desenvolvimento:
	- Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar(ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e teste novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;
    
Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
	- Red;
    - Green;
    - Refactor
	
    
    
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f"{self.__nome} está miando...")


# Testes manuais
felix = Gato("Felix")
print(felix.nome)
felix.miar()
