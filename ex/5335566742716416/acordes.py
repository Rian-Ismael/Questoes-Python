def my_in(elemento, lista):
    for carac in lista:
        if carac == elemento:
            return True
    return False


def acordes(musica_1, musica_2):
    acordes = []
    for i in range(len(musica_1)):
        acordes.append(musica_1[i])
    for j in range(len(musica_2)):
        if not my_in(musica_2[j], acordes):
            acordes.append(musica_2[j])
    return acordes
