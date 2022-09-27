fator = int(input())

i = 0
while True:
    produto = i * fator
    print(f"{fator}  x {i:2}  = {produto:3}")
    if i >= 10:
        break
    else:
        i += 1
