def my_remove(e, lista):
    for i in range(len(lista)-1, -1, -1):
        if e == lista[i]: lista.pop(i)
    return lista

valor = [1, 5, 4]
print(my_remove(4, valor))