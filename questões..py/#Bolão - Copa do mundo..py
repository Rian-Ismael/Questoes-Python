#Bolão - Copa do mundo.

placar_real = int(input()) #AxB --> Time A, Time B.
palpite = int(input()) #AxB --> Time A, Time B.

timeA_real = placar_real[0]
timeB_real = placar_real[2]

timeA_palpite = palpite[0]
timeB_palpite = palpite[2]

if timeA_real == timeA_palpite:
    soma = timeA_real+timeA_palpite