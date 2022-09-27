def my_in(elemento, lista):
    for num in lista:
        if num == elemento:
            return True
    return False


def vogais_primeiro(frase):
    vogais = ""
    consoantes = ""
    vog = "aeiouAEIOU"
    for carac in frase:
        if my_in(carac, vog):
            vogais += carac

        else:
            consoantes += carac
    
    return vogais+consoantes

print(vogais_primeiro("exemplo"))