"""
def aleatorio(vetor):
    return list(set(vetor))

print(aleatorio([2, 3, 4, 2, 3]))
"""

def remove_duplicatas(lista):
    lista_sem_duplicatas = []
    for elemento in lista:
        if elemento not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(elemento)
    return lista_sem_duplicatas

print(remove_duplicatas([2, 3, 4, 2, 3]))
