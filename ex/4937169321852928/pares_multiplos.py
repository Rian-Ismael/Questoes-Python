# pares múltiplos
recebe = input()
fator = int(input())


inteiros = []
multiplos = []
pares = 0
sequencia = recebe.split()
for j in range(len(sequencia)):
    inteiros.append(int(sequencia[j]))
for i in range(len(inteiros)):
    if i < len(sequencia)-1:
        if (inteiros[i] * fator) == inteiros[i+1]:
            multiplos.append(sequencia[i])
            multiplos.append(sequencia[i+1])
            pares += 1

        elif (inteiros[1+i] * fator) == inteiros[i]:
            multiplos.append(sequencia[i])
            multiplos.append(sequencia[i+1])
            pares += 1

print(pares, "par(es)")
for par in range(0, len(multiplos), 2):
    if par < len(multiplos)-1:
        print(f"{multiplos[par]} {multiplos[par+1]}")
