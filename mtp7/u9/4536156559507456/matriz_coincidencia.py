def matriz_coincidencia(M1, M2):
  M = []
  for i in range(len(M1)):
    linha_M1 = M1[i]
    linha_M2 = M2[i]
    linha = []
    for j in range(len(M2)):
      elem_M1 = linha_M1[j]
      elem_M2 = linha_M2[j]
      if elem_M1 == elem_M2: 
        linha.append(elem_M1)
      else:
        linha.append(0)
    M.append(linha)

  return M
