test_meu.py

questao.py


from undertst import diff_simetricos

def test_lista_vazia():
    lista0 = []
    assert diff_simetricos(lista0) == []
    assert lista0 == []


def test_lista_de_apenas_um_valores():
    lista1 = [1]
    assert diff_simetricos(lista1) == [1]
    assert lista1 == [1]


def test_lista_de_dois_valores():
    lista2 = [1, 2]
    assert diff_simetricos(lista2) == [-1]
    assert lista2 == [1, 2]


def test_lista_de_tres_valores():
    lista3 = [2, 4, 5]
    assert diff_simetricos(lista3) == [-3, 4]
    assert lista3 == [2, 4, 5]


def test_lista_quatro_valores():
    lista4 = [1, 10 , 100, 200]
    assert diff_simetricos(lista4) == [-199, -90]
    assert lista4 == [1, 10, 100, 200]


def test_lista_cinco_valores():
    lista5 = [1, 2, 0, 0, 0]
    assert diff_simetricos(lista5) == [1, 2, 0]
    assert lista5 == [1, 2, 0, 0, 0]


def test_varios_nulos():
    lista6 = [0, 0, 0, 0, 0]
    assert diff_simetricos(lista6) == [0, 0, 0]
    assert lista6 == [0, 0, 0, 0, 0]


def test_um_nulo():
    lista7 = [0]
    assert diff_simetricos(lista7) == [0]
    assert lista7 == [0]


def test_tamanho_par_de_nulos():
    lista8 = [0, 0]
    assert diff_simetricos(lista8) == [0]
    assert lista8 == [0, 0]


def test_tamanho_muio_grande():
    lista9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert diff_simetricos(lista9) == [-9, -7, -5, -3, -1]
    assert lista9 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_liata_de_zero_a_dez():
    lista10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert diff_simetricos(lista10) == [-10, -8, -6, -4, -2, 5]
    assert lista10 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_decrescente_tamanho_impar():
    lista11 = [10, 9, 8, 7, 6]
    assert diff_simetricos(lista11) == [4, 2, 8]
    assert lista11 == [10, 9, 8, 7, 6]


def test_decrescente_tamanho_par():
    lista12 = [10, 9, 8, 7]
    assert diff_simetricos(lista12) == [3, 1]
    assert lista12 == [10, 9, 8, 7]