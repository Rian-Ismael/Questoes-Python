def meu_in(lista, elemento):
  i = 0
  while (i < len(lista)):
    if (lista[i] == elemento):
      return True
    i += 1
  return False

palavra = input()
total_palavras = 0

while True:
  consoantes = 0
  vogais = 0
  i = 0
  while (i < len(palavra)):
    if (meu_in(['a','e','i','o','u'], palavra[i].lower())):
      vogais += 1
    else:
      consoantes += 1
    i += 1
print(total_palavras)