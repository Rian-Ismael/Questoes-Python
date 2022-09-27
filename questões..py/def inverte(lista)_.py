def inverte(lista):
    invertido = []
    for i in range(len(lista)-1, -1, -1):
        invertido.append(lista[i])
    return invertido


def caracol(matriz):
    saida = []
    for i in range(len(matriz)):
        if i % 2 != 0:
            saida.append(inverte(matriz[i]))
        else:
            saida.append(matriz[i])

    valores = []
    for i in range(len(saida)):
        for j in range(len(saida[i])):
            valores.append(saida[i][j])
    
    nova_lista_matrizZero = []
    resto = []
    for i in range(len(valores)):
        if i <= len(matriz[0]):
            nova_lista_matrizZero.append(valores[i])
        else:
            resto.append(valores[i])


    resto_invertido = inverte(resto)
    return nova_lista_matrizZero+resto_invertido
    
M2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
M3 = [[1, 2], [3, 4]]
M4 = [[1, 2, 7], [3, 4, 5]]
print(caracol(M4))
assert caracol(M3) == [1, 2, 4, 3]
assert caracol(M2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]