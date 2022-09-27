a = int(input())
b = int(input())
c = int(input())

def soma_perimetro(a,b,c):
    soma = a+b+c
    return soma

perimetro = int(soma_perimetro(a,b,c))

if  a < (b+c) and b < (a+c) and c < (b+a):
  print('triangulo valido. {}'.format(perimetro))

else:
  print('triangulo invalido.')

