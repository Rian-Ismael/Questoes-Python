def reduz_matriz(m):
  elementos_removidos = 0
  if (len(m) >= 5):
    elementos_removidos += len(m.pop(0))
    elementos_removidos += len(m.pop(-1))
  elif (len(m) == 4):
    elementos_removidos += len(m.pop(0))

  if (len(m[0]) >= 5):
    for linha in m:
      linha.pop(0)
      elementos_removidos += 1
    for linha in m:
      linha.pop(-1)
      elementos_removidos += 1
  elif (len(m[0]) == 4):
    for linha in m:
      linha.pop(0)
      elementos_removidos += 1

  return elementos_removidos
