tensao1 = int(input())
resist1 = int(input())

tensao2 = int(input())
resist2 = int(input())

tensao3 = int(input())
resist3 = int(input())

corrente1 = tensao1 / resist1
corrente2 = tensao2 / resist2
corrente3 = tensao3 / resist3

if corrente1 > corrente2 and corrente1 > corrente3:
    maior_valor = corrente1    
    condutor = "1"
elif corrente2 > corrente1 and corrente2 > corrente3:
    maior_valor = corrente2
    condutor = "2"
else:
    maior_valor = corrente3
    condutor = "3"


if maior_valor < 0.001:
    conversao = maior_valor*1000000
    unidade = "µA"

elif maior_valor < 1:
    conversao = maior_valor*1000
    unidade = "mA"

else:
    conversao = maior_valor
    unidade = "A"

print(f"condutor com maior corrente: {condutor}\nmaior corrente: {conversao:.2f} {unidade}")
