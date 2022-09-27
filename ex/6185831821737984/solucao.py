def my_split(stri):
    saida = []
    elemento = ""
    for i in range(len(stri)):
        if stri[i] == " ":
            saida.append(elemento)
            elemento = ""

        else:
            elemento += stri[i]
    saida.append(elemento)

    return saida


def count(phrase):
    cont = 0
    for i in range(len(phrase)):
        cont += 1

    return cont


def maior_palavra(frase):
    lista = my_split(frase)
    maior = count(lista[0])
    indice = None
    for i in range(len(lista)):
        if count(lista[i]) >= maior:
            indice = i
            maior = (count(lista[i]))

    return (lista[indice])
