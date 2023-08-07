"""
Introdução ao módulo Unittest

Unittest - > Testes Unitários

O que são testes unitário?
> Teste Unitário é forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

Obs: Teste unitário não é especifico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir de então ganhamos todos os "assertions" presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Suites de teste para sua unidade


Alguns métodos:					Checa se:
https://docs.python.org/3/library/unittest.html

assertEqual(a,b)				a == b
assertNotEqual(a,b)				a != b
assertTrue(x)					bool(x) is True
assertFalse(x)					bool(x) is False


Por convenção, todos os testes em um test case, devem ter seu nome iniciado com test_
O ideal é separar os testes, ou seja, criar dois métodos ao invés de criar um método com dois testes.


# Para executar os teste com unittest
> python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose
> python nome_do_modulo.py -v


# Docstring nos testes
Podemos acrescentar (e é recomendado) docstrings nos nossos testes


Method                      Checks that

assertEqual(a, b)           a == b 
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isinstance(a, b)

"""


###### Prática - Utilizando a abordagem TDD ######
import unittest
from atividades import comer, dormir, engracado


# Criar uma classe (mesmo nome do módulo - convenção)

class AtividadesTestes(unittest.TestCase):
    # NÃO IDEAL, 1 método e vários testes
    # def test_comer(self):
    #     self.assertEqual(
    #         comer("quiabo", True),
    #         "Estou comendo quiabo porque quero manter a forma"
    #     )

    #     self.assertEqual(
    #         comer(comida='pizza', saudavel=False),
    #         "Estou comendo pizza porque a gente só vive uma vez"
    #     )
    def test_comer_saudavel(self):
        """
        Testando o retorno com comida saudavel

        """
        self.assertEqual(
            comer("quiabo", True),
            "Estou comendo quiabo porque quero manter a forma"
        )

    def test_comer_nao_saudavel(self):
        """
        Testando o retorno com comida não saudavel

        """
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            "Estou comendo pizza porque a gente só vive uma vez"
        )

    def test_dormir_pouco(self):
        """
        Testando o retorno dormindo pouco

        """
        self.assertEqual(
            dormir(4),
            "Continuo cansado após dormir 4 horas"
        )

    def test_dormir_muito(self):
        """
        Testando o retorno dormindo muito

        """
        self.assertEqual(
            dormir(10),
            "Dormi muito"
        )

    def test_engracado(self):
        # self.assertEqual(engracado("Sergio Malandro"), False)
        self.assertFalse(engracado("Sergio Malandro"))
        self.assertTrue(engracado("Jim Carrey"),
                        "Jim Carrey deveria ser engracado")


if __name__ == '__main__':
    unittest.main()
