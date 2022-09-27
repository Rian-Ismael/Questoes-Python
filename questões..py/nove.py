def copia(lista):
  aux = []
  for i in range(len(lista)):
    aux.append(lista[i])
  return aux

def insere_ordenado(numero, lista):
    lista.append(numero)

    for i in range(len(lista) -1, 0, -1):
        if lista[i] > lista[i - 1]:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]


def soma_primeiros(lista):
    if len(lista) > 1:
        soma = lista[0] + lista[1]
        lista.pop(1)
    else:
        soma = lista[0]

    lista.pop(0)
    return soma


def noves_fora(lista):
    progresso = [lista[:]]
    soma = 0

    if len(lista) < 2: 
        soma = soma_primeiros(lista) % 9
        if progresso[0][0] >= 9:
            insere_ordenado(soma, lista)
            progresso.append(copia(lista))

    for i in range(len(lista) - 1):
        soma = soma_primeiros(lista) % 9
        insere_ordenado(soma, lista)
        progresso.append(copia(lista))

    return (soma, progresso)


assert noves_fora([9, 7, 5, 4, 3, 1])
assert noves_fora([4]) == (4, [[4]])
assert noves_fora([9]) == (0, [[9], [0]])
assert noves_fora([9, 9]) == (0, [[9, 9], [0]])