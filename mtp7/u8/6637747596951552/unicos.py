def meu_in(lista, elemento):
  for elem in lista:
    if elem == elemento: return True
  return False

def meu_count(lista, elemento):
  count = 0
  for elem in lista:
    if elem == elemento: count += 1
  return count

def unicos_em_comum(seq1, seq2):
  em_comum_seq1 = []
  for elem in seq1:
    if meu_count(seq1, elem) == 1:
      if not meu_in(em_comum_seq1, elem):
        em_comum_seq1.append(elem)
  
  em_comum_seq2 = []
  for elem in seq2:
    if meu_count(seq2, elem) == 1:
      if not meu_in(em_comum_seq2, elem):
        em_comum_seq2.append(elem)
  
  em_comum = []
  for i in range(len(em_comum_seq1)):
    if meu_in(em_comum_seq2, em_comum_seq1[i]):
      em_comum.append(em_comum_seq1[i])

  return em_comum

seq1 = [ 'A', 'A', 'B', 'C', 'C', 'D']
seq2 = ['B', 'A', 'C', 'D', 'D']
assert unicos_em_comum(seq1, seq2) == ['B']

seq1 = ['A', 'A', 'B', 'C']
seq2 = ['A', 'B', 'C']
assert unicos_em_comum(seq1, seq2) == ['B', 'C']  
