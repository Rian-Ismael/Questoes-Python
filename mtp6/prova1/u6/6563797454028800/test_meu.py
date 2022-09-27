from diff import diff_simetricos


def test_c1():
    assert diff_simetricos([2, 5 ,3, 9]) == [-7, 2]
    assert diff_simetricos([2, 5 ,3, 9, 4]) == [-2, -4, 3]


def test_lista_vazia():
    assert diff_simetricos([]) == [] # Lista vazia

def test_tamanho_par_num_diferentes():  
    assert diff_simetricos([1, 2, 3, 4]) == [-3, -1] # Tamanho par e números diferentes

def test_tamanho_impar_num_diferentes():
    assert diff_simetricos([1, 2, 3, 4, 5]) == [-4, -2, 3] # Tamando ímpar e números diferentes 
  
def test_tamanho_par_num_iguais():
    assert diff_simetricos([2, 2, 2, 2]) == [0, 0] # Tamanho par e números iguais 

def test_tamanho_impar_num_iguais():
    assert diff_simetricos([2, 2, 2, 2, 2]) == [0, 0, 2] # Tamanho ímpar e números iguais

def test_tamanho_par_num_diferentes_negativos():
    assert diff_simetricos([-1, -2, -3, -4]) == [3, 1] # Tamanho par e números diferentes e negativos

def test_tamanho_impar_num_diferentes():
    assert diff_simetricos([-1, -2, -3, -4, -5]) == [4, 2, -3] # Tamando ímpar e números diferentes e negativos

def test_tamanho_par_num_iguais_negativos():
    assert diff_simetricos([-2, -2, -2, -2]) == [0, 0] # Tamanho par e números iguais e negativos

def test_tamanho_impar_num_iguais_negativos():
    assert diff_simetricos([-2, -2, -2, -2, -2]) == [0, 0, -2] # Tamanho ímpar e números iguais e negativos

def test_tamanho_par():
    assert diff_simetricos([1, -2, 3, -4]) == [5, -5] 

def test_tamanho_impar():
    assert diff_simetricos([1, -2, 3, -4, 5]) == [-4, 2, 3]

def test_numeros_negativos():
    assert diff_simetricos([-1, 2, -3, 4]) == [-5, 5] 

def test_numeros_positivos():
    assert diff_simetricos([-1, 2, -3, 4, -5]) == [4, -2, -3]

def test_c15():
    assert diff_simetricos([2, -2, 2, -2]) == [4, -4] 

def test_c16():
    assert diff_simetricos([2, -2, 2, -2, 2]) == [0, 0, 2]

def test_c17():
    assert diff_simetricos([-2, 2, -2, 2]) == [-4, 4] 

def test_c18():
    assert diff_simetricos([-2, 2, -2, 2, -2]) == [0, 0, -2]
