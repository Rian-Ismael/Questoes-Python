def conta_alertas_acude(medicoes):
    alarme = 0
    for i in range(len(medicoes)-1, -1, -1):
        if medicoes[i] < 17:
            if abs(medicoes[i] - medicoes[i-1]) < 10:
                alarme += 1

    return alarme
