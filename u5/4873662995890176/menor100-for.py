i = 1
for linha in open("dados.dat"):
    linha = int(linha)
    if linha < 100: break
    i += 1

print(f"{linha}, na posição {i}")
