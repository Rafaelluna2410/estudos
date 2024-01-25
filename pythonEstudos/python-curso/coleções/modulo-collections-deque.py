'''
Módulo Collections - Deque

É uma lista de alta performace

'''

from collections import deque

# Criando deques

deq = deque('Geek')
print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final

deq.appendleft('k') # Adiciona no começo

# Remover elementos

print(deq.pop()) # Remove e retorna o último elemento
print(deq)

print(deq.popleft()) # Remvoe e retorna o primeiro elemento

print(deq)
