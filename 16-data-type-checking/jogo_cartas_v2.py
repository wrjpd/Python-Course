"""

v2 -> Funções com Type Hints

"""
import random
from typing import Dict, List, Tuple, Set

naipes: List[str] = f"\u2660 \u2665 \u2666 \u2663".split()
cartas: List[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()

carta = Tuple[str, str]
baralho = List[carta]


def criar_baralho(aleatorio: bool = False) -> baralho:
    """Criar baralho com 52 Cartas"""
    baralho = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def separa_cartas(baralho: baralho) -> Tuple[baralho, baralho, baralho, baralho]:
    """ Separa cartas para 4 mãos"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


# baralho = criar_baralho()
# print(separa_cartas(baralho))


def jogar() -> None:
    """Inicia um jogo de cartas par 4 jogadores"""
    cartas: baralho = criar_baralho(aleatorio=True)
    jogadores: List[str] = "P1 P2 P3 P4".split()
    maos: Dict[str, baralho] = {j: m for j,
                                m in zip(jogadores, separa_cartas(cartas))}
    # print(maos.items())
    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}"for (j, c) in cartas)
        print(f"{jogador}:{carta}")
    # for jogador,cartas in maos.items()


if __name__ == "__main__":
    jogar()
