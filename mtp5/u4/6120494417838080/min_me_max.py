n = int(input())

minimo, soma, maximo = 9999999999, 0, -9999999999
for i in range(1, n+1):
  x = int(input())
  soma += x
  if(x < minimo):
    minimo = x
  if (x > maximo):
    maximo = x
  
  print(f"{x} {minimo} {(soma/i):.2f} {maximo}")
