from undertst import caracol

def test_1():
    M2 = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
    assert caracol(M2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        
