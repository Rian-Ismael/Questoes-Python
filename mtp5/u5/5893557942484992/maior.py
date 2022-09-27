maior_palavra = ""
tamanho_maior_palavra = 0
conjunto_maior_palavra = 1
conjuntos = 1
while True:
  palavra = input()
  if (palavra == "fim"):
    break
  elif palavra == "---":
    conjuntos += 1
  else:
    if (len(palavra) == tamanho_maior_palavra):
      continue
    elif (len(palavra) > tamanho_maior_palavra):
      maior_palavra = palavra
      tamanho_maior_palavra = len(palavra)
      conjunto_maior_palavra = conjuntos

if (conjuntos == 1 or tamanho_maior_palavra == 0 or maior_palavra == "" ):
  pass
else:  
  print(f"Conjunto {conjunto_maior_palavra}: {maior_palavra} ({tamanho_maior_palavra} letras)")

