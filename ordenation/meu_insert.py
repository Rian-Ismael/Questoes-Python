def meu_insert(lista, posicao, elemento):
    lista.append(elemento)
    for i in range(len(lista)-1, posicao, -1):
        lista[i], lista[i-1] = lista[i-1], lista[i]
        
    return lista
