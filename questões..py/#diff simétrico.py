#diff simétrico

lista1 = [3, 8, 3, 5, 9]
lista2 = [3, 8, 7, 4]
lista3 = [-1, -5, -6, -8, -9]

def diff(valores):
    lista_nova = []
    meio = int(len(valores) / 2)
    for i in range(meio):
        diferenca = valores[i] - valores[len(valores) - 1 - i]
        lista_nova.append(diferenca)
        if len(valores) % 2 != 0:
            lista_nova.append(valores[meio])
    return lista_nova
            

print(diff(lista1))