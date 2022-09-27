import math
print("Cálculo da Superfície de um Cilindro"'\n---')

diametro = float(input("Medida do diâmetro? "))
raio = float(diametro / 2)
altura = float(input("Medida da altura? "))

area_cilindro = 2*(math.pi * raio ** 2) + 2*(math.pi * raio * altura)

print("---\n"f'Área calculada:{area_cilindro: .2f}')




