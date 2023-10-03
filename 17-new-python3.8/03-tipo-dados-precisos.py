"""
# Tipos de dados mais precisos

- Literal type - Indica que a variável tem um valor específico e concreto Literal[3], Literal['conectado',desconectado']
- Union - Indica multipls tipos - Union[str,int]
- Final - Indica que o nome é uma constante
- Typed dictionaries - Dicionários em classes
- Protocols - Modela um comportamento


# @final decorator

@final podem ser usados para decorar classes ou métodos.
-> @final em classes indica que nenhuma outra classe pode estender ela;



-> @final em métodos indica que classes filhas dessa classe não podem sobreescrever o método.

"""


from typing import Literal, Union, Final, final, TypedDict, Protocol

### Literal Type ###


def pegar_status(usuario: str) -> Literal["conectado", "desconectado"]:
    pass


def calcula(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == "+":
        print(f"{num1}+{num2}={num1+num2}")
    elif operacao == "-":
        print(f"{num1}-{num2}={num1-num2}")


# calcula('*', 2, 3)  # Alerta


### Union ###

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1+num2

    if resultado > 58:
        return f"O valor {resultado} é muito grande."
    else:
        return resultado


### Final ###

nome: Final = "Geek"
# teste = 3  # Erro pq estamos reatribuindo
print(nome)


### final decorator ###

# Classe -> error: Cannot inherit from final class "Pessoa"  [misc]
@final
class Pessoa:
    pass


class Estudante(Pessoa):
    pass


# Método
class Animal:
    @final
    def comer(self):
        print("estou comendo")


class Cavalo:
    def comer(self):
        print("estou comendo capim")


### Typed Dictionaries ###

class CursoPython(TypedDict):
    versao: str
    atualizacao: int

    def __init__(self, nome):
        self.__nome = nome


geek = CursoPython(versao="3.8.8", atualizacao=2020, nome="Geek")
print(geek)


### Protocols ###

class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f"Estou estudando o curso {valor.titulo}")


class Venda:
    titulo = 2


# c1 = Curso() #Protocols cannot be instantiated

v1 = Venda()
estudar(v1)
