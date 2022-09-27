# telefonia
# R$ 1 real de taxa fixa
# ligação <= 3 min: R$ 0.50 reais por minuto
# ligação > 3 min:
# cada bloco de 5 minutos serão cobrados R$ 3 reais
# Bloco com menos de 5 minutos serão cobrados R$ 0.70 por minuto

minuto = int(input())

if minuto <= 3:
    menos_3_minutos = 0
    for _ in range(minuto):
        menos_3_minutos += 0.50

    gasto_total_menos_3_minutos = (1 + menos_3_minutos)
    print(f"R$ {gasto_total_menos_3_minutos:.2f}")

elif (minuto) > 3:
    bloco = minuto // 5
    resto = minuto % 5
    mais_3_minutos = 0
    for _ in range(bloco):
        mais_3_minutos += 3.00

    for _ in range(resto):
        mais_3_minutos += 0.70
        
    gasto_total_mais_3_minutos = (1 + mais_3_minutos)
    print(f"R$ {gasto_total_mais_3_minutos:.2f}")
