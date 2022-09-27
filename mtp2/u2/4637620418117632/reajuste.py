salario_atual = float(input())
novo_valor = float(input())

reajuste = 100 * (novo_valor - salario_atual) / salario_atual

print(f'Reajuste de {reajuste:.1f}%')
