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
