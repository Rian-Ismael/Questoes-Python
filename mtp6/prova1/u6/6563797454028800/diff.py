#Rian Ismael Elias de Melo
#Questão: Diff Simétricos
#rian.melo@ccc.ufcg.edu.br


lista1 = [3, 4, 2, 4]
print(len(lista1))
print(int(len(lista1)/2))
def diff_simetricos(valores):
  saida = []
  metade_tamanho_lista = int(len(valores)/2)
  for i in range(metade_tamanho_lista):
    saida.append(valores[i] - valores[len(valores)-i-1])
  if len(valores) % 2 != 0:
    saida.append(valores[metade_tamanho_lista])

  return saida

print(diff_simetricos(lista1))
