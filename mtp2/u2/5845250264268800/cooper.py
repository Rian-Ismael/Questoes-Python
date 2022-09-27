import math

valor_raio = float(input())
quantidade_voltas = float(input())

circun = 2*math.pi*valor_raio*quantidade_voltas

print(f'A pessoa percorreu {circun:.3f} metros.')
