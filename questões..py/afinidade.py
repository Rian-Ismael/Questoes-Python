def busca(elemento, lista2):
    for music2 in lista2:
        if elemento == music2:
            return True
 
    return False
 
 
def tem_afinidade(lista1, lista2):
    cont = 0
    for music1 in lista1:
        if busca(music1, lista2):
            cont += 1
    if cont >= 3:
        return True
  
    return False
  
l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True
