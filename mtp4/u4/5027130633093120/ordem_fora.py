palavras = input().split(' ')

em_ordem = True
for i in range(len(palavras)-1):
  palavra_atual = palavras[i]
  prox_palavra = palavras[i+1]
  if (palavra_atual > prox_palavra):
      em_ordem = False
      break
  
if em_ordem:
  print("em ordem")
else:
  print("fora de ordem:", i+2)
