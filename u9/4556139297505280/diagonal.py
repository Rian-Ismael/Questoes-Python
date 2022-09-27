def diagonais(M):
    matriz_diagonais = []
    diagonal_principal = []
    diagonal_secundaria = []
    for i in range(len(M)):
        diagonal_principal.append(M[i][i])
        diagonal_secundaria.append(M[i][len(M)-1-i])
    matriz_diagonais.append(diagonal_principal)
    matriz_diagonais.append(diagonal_secundaria)
    
    return matriz_diagonais
