from comeram import quantos_comeram

def test_c1():
    assert quantos_comeram(10, [10, 10]) == 10

def test_c2():
    assert quantos_comeram(12, [10, 10]) == 10

def test_c3():
    assert quantos_comeram(2, [10, 10]) == 0

def test_c4():
    assert quantos_comeram(5, [2, 3, 5]) == 5

def test_c5():
    assert quantos_comeram(2, [1, 5, 8]) == 1

def test_c6():
    assert quantos_comeram(2, [2, 5, 8]) == 2

def test_c7():
    assert quantos_comeram(10, [11, 10]) == 0

def test_c8():
    assert quantos_comeram(10, []) == 0
