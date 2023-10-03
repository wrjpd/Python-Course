"""

v1 -> Funções com Python "normal" sem Type Hints

"""
import random
from typing import Dict, List, Tuple, Set

naipes = f"\u2660 \u2665 \u2666 \u2663".split()
cartas = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def criar_baralho(aleatorio=False : bool) -> :
    """Criar baralho com 52 Cartas"""
    baralho = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def separa_cartas(baralho):
    """ Separa cartas para 4 mãos"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


baralho = criar_baralho()
# print(separa_cartas(baralho))


def jogar():
    """Inicia um jogo de cartas par 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = "P1 P2 P3 P4".split()
    maos = {j: m for j, m in zip(jogadores, separa_cartas(cartas))}
    # print(maos.items())
    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}"for (j, c) in cartas)
        print(f"{jogador}:{carta}")
    # for jogador,cartas in maos.items()


if __name__ == "__main__":
    jogar()
