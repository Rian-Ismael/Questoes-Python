def matriz(n_lin, n_col):
    return [[None for i_col in range(n_col)] for i_lin in range(n_lin)]


def matriz_coincidencia(M1, M2):
    matriz_nova = matriz(len(M1), len(M2[0]))
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if M1[i][j] == M2[i][j]:
                matriz_nova[i][j] = M1[i][j]
            else:
                matriz_nova[i][j] = 0

    return matriz_nova
    

M1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

M2= [[10, 11, 12],
     [13, 14, 15]]

M3= [[10, 3],
     [13, 14, 15]]
print(matriz_coincidencia(M2, M3))
# assert matriz_coincidencia(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]
# print(matriz_coincidencia(M1, M2))
# assert matriz_coincidencia(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]
# print(matriz_coincidencia(M1, M3))