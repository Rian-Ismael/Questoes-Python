def bubblesort(dados):
    for i in range(len(dados)-1, -1, -1):
        troca = False
        for j in range(0, i):
            if dados[j+1] < dados[j]:
                dados[j], dados[j+1] = dados[j+1], dados[j]
                troca = True

        if not troca:
            break

    return dados
