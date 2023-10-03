"""
Duck Typing - Se um objeto parece como pato, nada como pato, anda como um pato, então é um pato
-> Objetos similares tem comportamentos similares

O Duck Typing está relacionado à tipagem dinâmica de dados
-> O tipo ou a classe de objeto é menos importante do que os métodos que o definem;
-> É checado a presença ou não de métodos ou atributos específicos;

"""


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()

print(len(livro))

# Não importa a classe ou objeto
nome = "Geek University"
lista = [12, 34, 55, 49]
dicio = {"carlos": 12, "Vanessa": 49}

print(len(nome))
print(len(lista))
print(len(dicio))
