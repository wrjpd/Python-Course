"""

Funções matemáticas e estatísticas

math.prod() -> Retorna o produto de um container numérico

math.isqrt() -> Retorna a parte inteira da raiz quadrada

math.dist() -> Retorna a distância euclidianda entre dois pontos.

math.hypot() -> Retorna a hipotenusa, ou norma euclidianda

statistics.fmean() -> Retorna a média de números reais

statistics.geometric_mean() -> Retorna a média geométrica

statistics.multimode() -> Retorna o valor mais frequente



"""
import math
import statistics


### math.prod ###
nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

### math.isqrt ###

print(f"{math.sqrt(12)=}")
print(math.isqrt(12))


### math.dist ###

# Pontos 3D

P3D1 = (12, 50, 40)
P3D2 = (6, 7, 13)
print(math.dist(P3D1, P3D2))

# Pontos 2D

P2D1 = [12, 50]
P2D2 = [6, 7]
print(math.dist(P2D1, P2D2))


### math.hypot ###
print(math.hypot(*P3D1))
print(math.hypot(*P2D1))


### Estatística ###

### statistics.fmean() ###
valores_reais = [1.45, 6.7, 8.9, 1.12]
valores_inteiros = [1, 6, 3, 89]


print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))


### statistics.geometric_mean() ###

print(statistics.geometric_mean(valores_inteiros))
print(statistics.geometric_mean(valores_reais))


### statistics.multimode ###

SEQ1 = "Geek University"
seq2 = [5, 3, 4, 3, 6, 3]
seq3 = [1, 2, 3, 4, 5]

print(statistics.multimode(SEQ1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
