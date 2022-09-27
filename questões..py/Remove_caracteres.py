def meu_in(elemento, lista):
        for e in lista:
                if (e == elemento): return True
        return False

def remove_caracteres(frase, caracteres):
        saida = ""
        for letra in list(frase):
                if not meu_in(letra, caracteres):
                        saida += letra
        return saida

frase = "Apalavrados"
assert remove_caracteres(frase, "sodA") == "palavra"