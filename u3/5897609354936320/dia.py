dia_semana_e_vendas = input().split()

semana = str(dia_semana_e_vendas[0])
vendas = int(dia_semana_e_vendas[1])


if vendas < 20:
    print("fraco")

elif vendas <= 30:
    print("normal")

elif semana == "sábado" or semana == "domingo":
    print("normal")

else:
    print("atípico")

