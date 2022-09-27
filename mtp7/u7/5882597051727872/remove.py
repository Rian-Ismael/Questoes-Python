def get_menor(lista):
  menor = lista[0]
  for num in lista:
    if num < menor:
      menor = num
  return menor

def remove_multiplos_do_menor(lista):
  menor = get_menor(lista)
  for i in range(len(lista)-1,-1,-1):
    if (lista[i] % menor == 0):
      lista.pop(i)
