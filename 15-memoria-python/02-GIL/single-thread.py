import time

contador = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()
print(f"Tempo sem segundos: {fim-inicio}")
