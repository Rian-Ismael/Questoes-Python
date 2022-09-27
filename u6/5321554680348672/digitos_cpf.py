def calcula_digitos_verificacao(cpf):
    inverso = []
    for i in range(len(cpf)):
        inverso.append(int(cpf[(len(cpf) - 1) - i]))
    
    aux = 2
    soma_um = 0
    for j in inverso:
        soma_um += (j*aux)
        aux += 1
    digito_um = ((soma_um*10) % 11)
    if digito_um == 10: 
        digito_um = 0 

    aux = 3
    soma_dois = (digito_um*2)
    for p in inverso:
        soma_dois += (p*aux)
        aux += 1
    digito_dois = ((soma_dois*10) % 11)

    if digito_dois == 10:    
        digito_dois = 0

    return f"{digito_um}{digito_dois}"
