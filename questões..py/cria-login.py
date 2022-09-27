def cria_login(usuario):
    login = ""
    nome = usuario.split()

    login += nome[0].lower()
    for i in range(1, len(nome)):
        if nome[i] != "de" and nome[i] != "do" and nome[i] != "da":
            login += nome[i][0].lower()

    return login


recebe = []
nome_completo = []
while True:
    entrada = input()
    nome_completo.append(entrada)
    if entrada == "fim":
        for i in range(len(recebe)):
            print(f"{nome_completo[i]}: {recebe[i]}")
        break
    else: 
        recebe.append(cria_login(entrada))

assert cria_login("Matheus Gaudencio do Rego") == "matheusgr"
assert cria_login("Eliane Araujo") == "elianea"
assert cria_login("Dalton Serey Guerrero") == "daltonsg"
assert cria_login("Diego dilva Pereira") == "diegodp"