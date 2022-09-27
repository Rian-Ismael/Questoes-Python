arq = open("dados.dat")

i = 1
while True:
    linha = arq.readline()
    linha = int(linha)
    if linha < 100: break
    i += 1


print(f"{linha}, na posição {i}")

