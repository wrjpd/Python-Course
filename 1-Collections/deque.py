"""

--- Módulo Collections - Deque ---

Deque --> Podemos dizer que o deque é uma lista de alta performance

"""

from collections import deque

deq = deque('geek')
print(deq)

# Adicionando elementos no começo
deq.appendleft('y')
print(deq)

# Removendo elementos no começo
deq.popleft()
print(deq)
