def encontra_maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior

def adiciona_maior(lista):
    diferenca = []
    for i in range(len(lista)-1):
        diferenca.append((lista[i] - lista[i + 1]))
    
    maior_absoluto = encontra_maior(diferenca)

    for i in range(len(lista)):
        lista[i] = lista[i] + maior_absoluto
    
    return None


l1 = [2, 6, 5, 4, 0, 1]
assert adiciona_maior(l1) == None
assert l1 == [6, 10, 9, 8, 4, 5]


##############################################



def adiciona_maior(lista):
    diferenca_absoluta = (lista[0] - lista[1])
    for i in range(len(lista) - 1):

        diferenca = (lista[i] - lista[i + 1])
        if (diferenca) > diferenca_absoluta:
            diferenca_absoluta = diferenca

    for i in range(len(lista)):
        soma = (lista[i] + diferenca_absoluta)
        lista[i] = soma
        

    return None

l1 = [2, 6, 5, 4, 0, 1]
assert adiciona_maior(l1) == None
assert l1 == [6, 10, 9, 8, 4, 5]