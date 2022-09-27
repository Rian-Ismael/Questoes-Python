# Programação 1 - 2021.2
# Rian Ismael Elias de Melo
# Matrícula: 12121019
# Questão: Maioridade penal

def maioridade_penal(lista_nomes, lista_idades):
    maior = []
    nomes = lista_nomes.split()
    idades = lista_idades.split()

    for i in range(len(idades)):
        if idades[i] >= "18":
            maior.append(nomes[i])

    maioridade = ""
    for nome in range(len(maior)):
        if nome == len(maior)-1:
            maioridade += maior[nome]
        else:
            maioridade += (maior[nome] + " ")

    return maioridade


assert maioridade_penal("Jansen Italo Ana", "14 21 60") == "Italo Ana"
assert maioridade_penal("amanda marilia rick", "14 15 12") == ""
assert maioridade_penal("melo pereira junior", "18 17 19") == "melo junior"
