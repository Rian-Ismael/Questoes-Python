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
