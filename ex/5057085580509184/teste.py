#Bolão - Copa do mundo.

placar_real = input() #AxB --> Time A, Time B. (Placar)
palpite = input() #AxB --> Time A, Time B. (Palpite)

realA = placar_real[0]
realB = placar_real[2]

palpiteA = palpite[0]
palpiteB = palpite[2]


if realA == palpiteA and realB == palpiteB:
    print(6)

elif realA > realB and palpiteA > palpiteB and palpiteA == realA:
    print(3)

elif realB > realA and palpiteB > palpiteA and palpiteB == realB:
    print(3)

elif realA > realB and palpiteA > palpiteB and palpiteA != realA:
    print(2)

elif realB > realA and palpiteB > palpiteA and palpiteB != realB:
    print(2)

else:
    print(0)
