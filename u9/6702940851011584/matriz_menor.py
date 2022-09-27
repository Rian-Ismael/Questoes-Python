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
