numero_de_palavras = int(input())


def busca(palavra):
    for i in range(len(palavra) - 1):
        if palavra[i] == palavra[i+1]:
            return True
    else:
        return False


normal_lista = []
n_lista = []
conta_n = 0
conta_normal = 0

for quantidade in range(numero_de_palavras):
    palavra = input()
    if busca(palavra):
        conta_n += 1
        n_lista.append(palavra)

    else:
        conta_normal += 1
        normal_lista.append(palavra)


print(f"{conta_n} palavra(s) com letras dobradas:")
for dobradas in n_lista:
    print(dobradas)

print("---")

print(f"{conta_normal} palavra(s) sem letras dobradas:")
for nao_dobradas in normal_lista:
    print(nao_dobradas)
