def separa_duas_cores(lista, cor1, cor2):
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == cor1:
            lista[len(lista)-i], cor1 = lista[len(lista)-i], cor1
    return lista
l1 = ['a', 'a', 'b', 'a', 'b']
print(separa_duas_cores(l1, 'b', 'a'))