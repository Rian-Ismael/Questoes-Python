dia_semana_e_vendas = input().split()

semana = str(dia_semana_e_vendas[0])
venda = int(dia_semana_e_vendas[1])

if venda < 20:
    movimento = 'fraco'

elif venda < 30:
    movimento = 'normal'

elif semana == 'sábado' or 'domingo' and venda < 20:
    movimento = 'fraco'
        else:
            movimento = 'normal'

else:
    movimento = 'atípico'

print(movimento)



