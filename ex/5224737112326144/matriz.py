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
