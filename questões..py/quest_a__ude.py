# se ele tá inscrito "inscritos" e a média >= 7.0

## se ele não tá inscrito "inscritos" e a média < 7.0

#     alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
# len(alunos): 6

# alunos[6]-1
############ efeito colateral
# pop(indice)

def meu_in(lista, elemento):
    for num in lista:
        if num == elemento:
            return True
    return False


def filtra_alunos(alunos, inscrito, media):
    eliminados = 0
    for i in range(len(alunos)-1, -1, -1):
        if (not meu_in(inscrito, alunos[i][0])) or (alunos[i][1] < media):
            eliminados += 1
            alunos.pop(i)

    return eliminados


inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
print(filtra_alunos(alunos, inscritos, 7.0))
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]