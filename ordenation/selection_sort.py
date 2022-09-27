def encontra_menor(lista, i):
    menor = i
    for i in range(menor + 1, len(lista)):
        if lista[i] < lista[menor]:
            menor = i
    return menor

def selection_sort(lista):
    for i in range(len(lista)):
        menor = encontra_menor(lista, i)
        lista[menor], lista[i] = lista[i], lista[menor]

    return lista

print(selection_sort([2, 5, 6, 1, -3]))

########################################################

def sort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
