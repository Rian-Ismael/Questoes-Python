def encontra_menores(num, lista):
    min = -1
    for i in lista:
        if i < num:
            min = i
            break

    return min

lista1 = [100, 200, 300, 400]
lista2 = [15, 12, 4, 9, 10]
lista3 = [10, 5, 7, 10] 
lista4 = [0, 2, -2, 3]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4
assert encontra_menores(7, lista3) == 5
assert encontra_menores(0, lista4) == -2

