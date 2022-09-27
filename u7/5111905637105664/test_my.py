from is_substring_expr import is_substring_expr

def test_1():
    assert is_substring_expr('oicvoce','oi*voce') == True

def test_2():
    assert is_substring_expr('oicarovoce','oi*voce') == True

def test_3():
    assert is_substring_expr('ttestetestado','teste*testado') == False

def test_4():
    assert is_substring_expr('testeiiiitestado', 'teste*testado') == True

def test_5():
    assert is_substring_expr('testeyytestadoo', 'teste*testado') == False
