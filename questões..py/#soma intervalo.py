def soma_intervalo(a, b):
    soma = 0
    for i in range(a, b+1):
        soma += i

    return soma


assert soma_intervalo(5, 15) == 110
assert soma_intervalo(10, 10) == 10
assert soma_intervalo(10, 11) == 21
assert soma_intervalo(0, 1) == 1
assert soma_intervalo(1, 0) == 0
assert soma_intervalo(2, 4) == 9
