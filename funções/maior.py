"""Buscar o numero maior de uma determinada lista"""

def calcule_maior(lista: int) -> int:
    maior = lista[0] #cameça com o primeiro elemento da lista sendo o maior dela
    for num in lista:
        if num > maior:
            maior = num
    return maior
