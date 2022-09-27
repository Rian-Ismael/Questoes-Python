def sum(lista):
    saida = 0
    for num in lista:
        saida += num
    return saida

def repetidos(matriz):
    elementos = []
    for i in range(len(matriz)):
        for e in range(len(matriz[0])):
            elementos.append(matriz[i][e])
   
    for elemento in elementos:
        cont = 0
        for i in range(len(elementos)):
            if elemento == elementos[i]:
                cont += 1
                if cont > 1:
                    return False
    return True

def eh_quadrado_magico(quadrado):
    if repetidos(quadrado) == False:
        return False
    else:
        comparador = sum(quadrado[0])
        saida = True
        sum_diagonais_esquerda = 0
        sum_diagonais_direita = 0
        for i in range(len(quadrado)):
            if sum(quadrado[i]) != comparador:
                saida = False

            sum_colun = 0
            for j in range(len(quadrado)):
                sum_colun += quadrado[j][i]
                if i == j: sum_diagonais_esquerda += quadrado[i][j]
                if i + j == len(quadrado)-1: sum_diagonais_direita += quadrado[i][j]

            if (sum_colun != comparador):
                saida = False

        if sum_diagonais_direita != comparador or sum_diagonais_esquerda != comparador:
            saida = False


    return saida


quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
quadrado2 = [[1,2,3],[4,5,6]]
assert eh_quadrado_magico(quadrado1)
assert not eh_quadrado_magico(quadrado2)

# quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
# len(3)-1 = 2

# i = 0
# j = 2

# i = 1
# j = 1

# i = 0
# j = 2