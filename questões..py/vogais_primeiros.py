def meu_in(elemento, lista):
        for e in lista:
                if (e == elemento): return True
        return False

def vogais_primeiro(frase):
        vogais, consoantes = "", ""
        for letra in list(frase):
                if meu_in(letra, ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']):
                        vogais += letra
                else:
                        consoantes += letra
        return vogais + consoantes

assert vogais_primeiro("exemplo") == "eeoxmpl"
assert vogais_primeiro("Programacao 1") == "oaaaoPrgrmc 1"
assert vogais_primeiro("rian") == "iarn"