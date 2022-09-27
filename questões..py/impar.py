lista = [1,2,3,4,5,6,7,8,9];

for indice in range(1, len(lista) - 1, 1):
  if lista[indice] % 2 == 0:
    lista.pop(indice);
    continue;
  lista[indice] *= 2;
  
print(lista)
