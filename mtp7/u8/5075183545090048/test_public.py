from undertst import rotdir

def test_exemplo():
    valores = [10, 20, 14, 17, 22, 9, 32]
    rotdir(valores)
    assert valores == [32, 10, 20, 14, 17, 22, 9]
        
