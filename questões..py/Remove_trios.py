def meu_in(elemento, lista):
    igual = 0
    for e in lista:
        if (e == elemento): 
            igual += 1
    return igual


def remove_trios(lista):
    nova_lista = lista
    for c in lista:
        if (meu_in(c, lista)) >= 3:
            nova_lista.pop(c)
    return nova_lista

assert remove_trios([1, 2, 3, 3, 3]) == [1, 2]
assert remove_trios([1, 1, 2, 1]) == [2]