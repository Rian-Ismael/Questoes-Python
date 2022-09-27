def matriz(n_lin, n_col):
    return [[None for i_col in range(n_col)] for i_lin in range(n_lin)]

def matriz_menor(M1, M2):
    matriz_nova = []
    for i in range(len(M1)):
        partes = []
        for j in range(len(M1[i])):
            if M1[i][j] < M2[i][j]:
                partes.append(M1[i][j])

            else:
                partes.append(M2[i][j])

        matriz_nova.append(partes)
        partes = []

    return matriz_nova


M1 = [[1, 2, 3], [13, 14, 15], [7, 8, 9]]

M2 = [[10, 11, 12], [4, 5, 6], [7, 8, 9]]

M3 = [[1, 2, 3], [0, 0, 0], [7, 8, 9]]

assert matriz_menor(M1, M2) == [[1,2,3],[4,5,6],[7,8,9]]

assert matriz_menor(M1, M3) == [[1,2,3],[0,0,0],[7,8,9]]