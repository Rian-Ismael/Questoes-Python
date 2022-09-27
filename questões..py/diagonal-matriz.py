def matriz(n_lin, n_col):
    [[None for i_col in range(n_lin)] for i_lin in range(n_lin)]

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

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

diagonais(M) == [[1,5,9],[3,5,7]]
print(diagonais(M))