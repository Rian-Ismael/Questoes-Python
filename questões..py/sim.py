def meu_in(elemento, lista):
    for num in lista:
        if num == elemento:
            return True
    return False


def intersecao_listas(lista1, lista2):
    for i in range(len(lista1)-1, -1, -1):
        if not meu_in(lista1[i], lista2):
            lista1.pop(i)


    return lista1


lista1 = [1, 3, 4]
lista2 = [4, 3]
intersecao_listas(lista1, lista2)
assert lista1 == [3, 4]