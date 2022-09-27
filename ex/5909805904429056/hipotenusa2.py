cateto1 = float(input("Cateto 1? "))
cateto2 = float(input("Cateto 2? "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2)

resultado = hipotenusa ** (1/2)

print(f'Hipotenusa: {resultado:.1f}')
