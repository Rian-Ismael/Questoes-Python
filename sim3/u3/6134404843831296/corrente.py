tensao1 = int(input())
resist1 = int(input())
tensao2 = int(input())
resist2 = int(input())
tensao3 = int(input())
resist3 = int(input())

corrente1 = float(tensao1 / resist1)
corrente2 = float(tensao2 / resist2)
corrente3 = float(tensao3 / resist3)

if corrente1 > corrente2:
    if corrente1 > corrente3:
        maior = corrente1

elif corrente2 > corrente1:
    if corrente2 > corrente3:
        maior = corrente2

elif corrente3 > corrente1:
    if corrente3 > corrente2:
        maior = corrente3

else:
    maior = corrente1

print(f"{maior}")

if maior < 1000:
    final = maior*1000
    print(f"{final}µA")
