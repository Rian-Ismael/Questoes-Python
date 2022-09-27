def matriz(n_lin, n_col):
    matriz_nova = []
    for i in range(n_lin):
        linha = []
        for j in range(n_col):
            linha.append(None)
    matriz_nova.append(linha)            


    return matriz_nova

def matriz(n_linha, n_col):
    return  [[None for i_col in range(n_col)] for i_lin in range(n_lin)]
