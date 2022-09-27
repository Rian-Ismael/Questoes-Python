def is_substring_expr(str1, str2):
    verifica1, verifica2 = str2.split("*")
    primeira = ""
    segundo = ""

    for letra in str1:
        if len(primeira) != len(verifica1):
            primeira += letra

    for letra in range(len(str1)-1, -1, -1):
        if len(segundo) != len(verifica2):
            segundo += str1[letra]

    segundo_inverso = ""
    for i in range((len(segundo)-1), -1, -1):
        segundo_inverso += segundo[i]

    # print(f"primeira: {primeira}, segundo: {segundo_inverso}")
    if primeira == verifica1 and segundo_inverso == verifica2:
        return True
    else:
        return False


assert is_substring_expr('oicvoce','oi*voce') == True
assert is_substring_expr('oicarovoce','oi*voce') == True
assert is_substring_expr('ttestetestado','teste*testado') == False
assert is_substring_expr('testeiiiitestado', 'teste*testado') == True
assert is_substring_expr('testeyytestadoo', 'teste*testado') == False
