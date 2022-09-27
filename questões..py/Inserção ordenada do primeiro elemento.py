def insere_ordenado_primeiro(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]

    return lista

l1 = [5,2,6,9,11,13]
print(insere_ordenado_primeiro(l1))
assert l1 == [2,5,6,9,11,13]

l2 = [3,1,2,4]
print(insere_ordenado_primeiro(l2))
assert l2 == [1,2,3,4]