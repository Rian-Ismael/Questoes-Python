def meu_sum(lista):
  soma = 0
  for num in lista:
    soma += num
  return soma

def eh_quadrado_magico(quadrado):
  eh_magico = 0
  valor = meu_sum(quadrado[0])
  
  for linha in quadrado: # linhas
    if meu_sum(linha) == valor:
      eh_magico += 1
  
  colunas = []
  for _ in range(len(quadrado)):
    l = []
    for i in range(len(quadrado)):
      l.append(quadrado[i][0])
    colunas.append(l)

  for coluna in colunas:  # colunas
    if meu_sum(coluna) == valor:
      eh_magico += 1

  diagonal_primaria = []
  for i in range(len(quadrado)): # diagonal primaria
    for j in range(len(quadrado)):
      if i == j: 
        
        diagonal_primaria.append(quadrado[i][j])

  if meu_sum(diagonal_primaria) == valor:
    eh_magico += 1

  diagonal_secundaria = []
  for i in range(len(quadrado)): # diagonal secundaria
    for j in range(len(quadrado)):
      if (i + j) == len(quadrado)-1 : 
        diagonal_secundaria.append(quadrado[i][j])

  if meu_sum(diagonal_secundaria) == valor:
    eh_magico += 1
    
  return eh_magico == len(quadrado) * 2 + 2
