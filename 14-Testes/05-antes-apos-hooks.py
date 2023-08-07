"""
Unittest - Antes e após hooks

Hooks são os testes em si, ou seja, a execução dos testes.

Métodos do unittest para trabalhar com isso:
setup() -> Executado antes de cada método de teste. É util para criarmos instâncias de objetos e outros dados;
tearDown() -> É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com banco de dados.

"""
import unittest
from robo import Robo


class RoboTest(unittest.TestCase):

    # setUp vai rodar antes de cada suite de teste
    # Para cada suite de teste estamos criando uma instância de Robo
    # Para utilizar a variavel criada em setUp, usamos self
    def setUp(self):
        self.megaman = Robo("Mega Man", bateria=50)
        print("setUp() sendo executado...")
        pass

    # tearDown vai rodar após cada suite de teste
    def tearDown(self):
        print("tearDown() sendo executado...")

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), "Eu sou o Mega Man")
        self.assertEqual(self.megaman.bateria, 49,
                         "A bateria deveria estar em 49%")


if __name__ == "__main__":
    unittest.main()
