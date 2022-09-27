capacidade_revestimento = float(input('Capacidade de revestimento? '))

print('\n== Dados do vão a revestir ==')

comprimento = float(input('Comprimento? '))
largura = float(input('Largura? '))
altura = float(input('Altura? '))


paredes = (2*largura*altura) + (2*comprimento*altura)
piso = comprimento*largura
area_total = paredes + piso
numero_caixas = int(area_total / capacidade_revestimento)

print('\n== Resultados ==')
print(f'Área total a revestir: {area_total:.1f} m2\nNúmero de caixas: {numero_caixas}')


