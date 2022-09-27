
# def my_insert(lista, elemento, posicao):
#     lista.append(elemento)
#     #lista = [3, 4, 5]
#     # len(lista): 3; posicao: 2; começa de 3 e vai até 2 == 1
#     for i in range(len(lista)-1, posicao, -1):
#         lista[i], lista[i-1] = lista[i-1], lista[i]

#     return lista

def my_join(lista):
    string = ''
    for carac in lista:
        string += carac
    return string


def inverte3a3(s):
    if len(s) % 3 == 0:
        tres_a_tres = []
        aux = ""
        cont = 0
        for i in range(len(s)):
            aux += s[i]
            cont += 1
            if cont == 3:
                tres_a_tres.append(aux)
                aux = ''
                cont = 0
        
        invertido = []
        for j in range(len(tres_a_tres)-1, -1, -1):
            invertido.append(tres_a_tres[j])

        return my_join(invertido)

print(inverte3a3('abcdef'))
