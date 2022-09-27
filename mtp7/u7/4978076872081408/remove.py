def remove_abaixo_media(l1):
    soma = 0
    for elemento in l1:
        soma += elemento
    media = soma/len(l1)    
    for i in range(len(l1)-1, -1, -1):
        if l1[i] < media:
            l1.pop(i)
    return l1


l1 = [1, 1, 1, -1, 1]
print(remove_abaixo_media(l1))
remove_abaixo_media(l1)
assert l1 == [1, 1, 1, 1]
