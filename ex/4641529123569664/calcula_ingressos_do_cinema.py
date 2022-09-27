adultos = float(input())
criancas = float(input())
ingresso_valor = float(input())

ingresso_adultos = adultos * ingresso_valor
ingresso_crianca = (criancas * ingresso_valor) / 2

valor_total = ingresso_adultos + ingresso_crianca

print(f'Total: R${valor_total: .2f}')
