def insere_ordenado(elemento, lista):
    lista.append(elemento)

    for i in range(len(lista)-1, 0, -1):
        if lista[i] < lista[i-1]:
            lista[i], lista[i-1] = lista[i-1], lista[i]

    return lista

print(insere_ordenado(4, [-1, 3, 5]))

##################################################

def insere_ordenado(lista, elemento):
    lista.append(elemento)
    j = len(lista)-1
    
    while j >0 and lista[j-1] > lista[j]:
        lista[j], lista[j-1] = lista[j-1], lista[j]
        j -= 1
     
    return lista
