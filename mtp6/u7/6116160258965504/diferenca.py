def meu_in(elemento, lista):
        for e in lista:
                if (e == elemento): return True
        return False

def diferenca_listas(lista1, lista2):
        diferenca = []
        for num in lista1:
                if meu_in(num, lista2):
                        diferenca.append(num)

        for num in diferenca: lista1.remove(num)

        return lista1
