def soma_intervalo(a, b):
    soma = 0
    for i in range((a+b)+1):
        if a <= i <= b:
            soma += i
    return soma

assert soma_intervalo(5, 15) == 110
assert soma_intervalo(10, 10) == 10
assert soma_intervalo(10, 11) == 21
assert soma_intervalo(0, 1) == 1
