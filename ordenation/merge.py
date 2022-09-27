def merge(lista1, lista2):
    lista3 = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            lista3.append(lista1[i])
            i += 1

        else:
            lista3.append(lista2[j])
            j += 1
    
    #i -- > lista1
    #j -- > lista2
    if i == len(lista1):
        for p in range(j, len(lista2)):
            lista3.append(lista2[p])

    else:
        for p in range(i, len(lista1)):
            lista3.append(lista1[p])

    return lista3


print(merge([0, 2, 3, 6, 7, 8, 9], [0, 1, 4, 5, 6, 7, 8, 9]))