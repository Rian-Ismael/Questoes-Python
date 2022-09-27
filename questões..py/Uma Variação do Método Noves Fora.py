def insere_ordenado(elemento, lista):
    lista.append(elemento)
    for j in range(len(lista)-1, -1, -1):
        for i in range(len(lista)-1, -1, -1):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista

def noves_fora(lista):
    #[8, 5, 2]; len = 3-1: 0, 1, 2
    saida = [tuple(lista)]
    if len(lista) >= 2:
        i = 0
        while i != (len(lista)):
            if len(lista) >= 2:
                soma = (lista[0]+lista[1])
                if (lista[0]+lista[1]) >= 9:
                    lista.pop(0)
                    lista.pop(0)
                    diferenca = (soma % (9))
                    insere_ordenado(diferenca, lista)
                    saida.append(tuple(lista))
                elif (soma) < 9:
                    lista.pop(0)
                    lista.pop(0)
                    insere_ordenado(soma, lista)
                    if len(lista) > 1:
                        saida.append(tuple(lista))
                if len(lista) < 2 and lista[0] != 0:
                    saida.append(tuple(lista))
                i += 1

            else:
                break
    
    elif len(lista) < 2 and lista[0] >= 9:
            diferenca = (lista[0] - (9))
            lista.pop(0)
            insere_ordenado(diferenca, lista)
            saida.append(tuple(lista))
    print(saida)
    saida2 = []
    for i in range(len(saida)):
        saida2.append(list(saida[i]))

    return lista[0], list(saida2)

print(noves_fora([9, 7, 5]))

