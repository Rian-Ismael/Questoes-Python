n1 = int(input())
n2 = int(input())
n3 = int(input())
  
if (n1 >= 0 and n2 >= 0 and n3 >= 0):
  if (n1+n2+n3 == 100):
    print('*')
  else:
    print(n1+n2+n3)
elif (n1 >= 0 and n2 >= 0 and n3 < 0):
  if (n1+n2 == 100):
    print('*')
  else:
    print(n1+n2)
elif (n1 >= 0 and n2 < 0):
  if (n1 == 100):
    print('*')
  else:
    print(n1)
else:
    print(0)
