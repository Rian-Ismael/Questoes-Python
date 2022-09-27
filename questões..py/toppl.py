# alunos: respectiva notas
# inscritos: lista dada, usa if in para analisar se está em alunos
# media mínima necessária

def my_in(elemento, lista):
    for num in lista:
        if num == elemento:
            return True
    return False

def filtra_alunos(alunos, inscritos, media):
    eliminados = 0
    for i in range(len(alunos)-1, -1, -1):
        if (alunos[i][1] < media) or (not my_in(alunos[i][0], inscritos)):
            alunos.pop(i)
            eliminados += 1

    return eliminados


inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]