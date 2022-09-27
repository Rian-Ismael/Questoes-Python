def par_impar(num):
    num = int(num)
    if num % 2 == 0:
        return True
    else: 
        return False


def senha_segura(senha):
    cont = 0
    if len(senha) % 2 == 0:
        i = 0
        while i != len(senha):
            if ((par_impar(senha[i])) == False) and ((par_impar(senha[i+1])) == True):
                cont += 1

            else:
                break
            i += 2 
    else:
        return "Senha insegura"   

    if cont == len(senha)//2:
        return "Senha segura"
    else:
        return "Senha insegura"
