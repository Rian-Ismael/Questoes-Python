# Se for >= 10 ela NÃO é confiável
# Se < 10 ela É confiável

def conta_alertas_acude(medicoes):
    alarme = 0
    for i in range(len(medicoes)-1, -1, -1):
        if medicoes[i] < 17:
            if abs(medicoes[i] - medicoes[i-1]) < 10:
                alarme += 1

    return alarme


medicoes = [50, 21, 13, 23, 21, 17, 15, 60, 65, 15, 15]
assert conta_alertas_acude(medicoes) == 3