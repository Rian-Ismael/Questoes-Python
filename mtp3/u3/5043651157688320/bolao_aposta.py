partida = input()
aposta = input()

gols_timeA, gols_timeB = int(partida[0]), int(partida[2])
aposta_gols_timeA, aposta_gols_timeB = int(aposta[0]), int(aposta[2])

if (gols_timeA == aposta_gols_timeA and gols_timeB == aposta_gols_timeB):
  print("6")
elif ((gols_timeA > gols_timeB and aposta_gols_timeA > aposta_gols_timeB) or
      (gols_timeA < gols_timeB and aposta_gols_timeA < aposta_gols_timeB)):
    if (gols_timeA == aposta_gols_timeA or gols_timeB == aposta_gols_timeB):
      print("3")
    else:
      print("2")
else:
  print("0")

