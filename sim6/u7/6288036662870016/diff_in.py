def meu_in(elemento, lista, j):
    for i in range(len(lista)):
        if lista[i] == elemento and i == j:
            return True
    return False


def idiff(seq1, seq2):
    indices = []
    if len(seq1) > len(seq2):
        for i in range(len(seq1)):
            if not meu_in(seq1[i], seq2, i):
                indices.append(i)
    else:
        for i in range(len(seq2)):
            if not meu_in(seq2[i], seq1, i):
                indices.append(i)

    return indices

seq1 = [10, 20, 30, 40, 50, 60, 70]
seq2 = [10, 20, 20, 40, 80]
assert idiff(seq1, seq2) == [2, 4, 5, 6]

sequencia1 = [1, 2]
sequencia2 = [2]
assert idiff(sequencia1, sequencia2) == [0, 1]

seque1 = [10, 20, 20, 40, 80]  
seque2 = [10, 20, 30, 40, 50, 60, 70]    
assert idiff(seque1, seque2) == [2, 4, 5, 6]
