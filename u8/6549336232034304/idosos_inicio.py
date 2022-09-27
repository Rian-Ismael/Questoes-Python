def idosos_inicio(fila):
    posicao = 0
    for i in range(len(fila)):
        if fila[i] >= 60: 
            fila[posicao], fila[i] = fila[i], fila[posicao]
            posicao += 1
