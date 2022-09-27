def split_simplificado(frase):
    split_simpl = []
    separado = ""
    for carac in frase:
        if carac == " ":
            split_simpl.append(separado)
            separado = ""

        else:
            separado += carac
        
    split_simpl.append(separado)

    return split_simpl