def divisor(num, lista):
    i = 0
    saida = -1
    while i != len(lista):
        if lista[i] % num == 0:
            saida = i
            break
        else:
            i += 1

    return saida


lista1 = [100,10,40,50]
lista2 = [3, 13, 50, 23, 5]
lista3 = [3, 0, 21, 7]
lista4 = [1, 2, 3, 4, 5]
assert divisor(10, lista1) == 0
assert divisor(5, lista2) == 2
assert divisor(7, lista3) == 1
assert divisor(5, lista4) == 4
