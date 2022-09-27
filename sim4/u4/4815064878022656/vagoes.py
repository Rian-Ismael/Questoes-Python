k = int(input())
vagoes = input().split()

inteiros = []
for e in range(len(vagoes)):
    inteiros.append(int(vagoes[e]))


cont = 0
for i in range(len(inteiros)-1):
    if abs((inteiros[i] - inteiros[i+1])) > k:
        cont += 1

print(cont)
