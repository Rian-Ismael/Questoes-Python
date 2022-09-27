soma = 0 
contador = 0

while soma < 20:
    num = int(input())

    soma += num
    contador += 1

print(f'{contador} - {soma}')

###########################

soma = 0
contador = 0

while True:
    num = int(input())

    soma += num
    contador += 1

    if soma >= 20: break

print(f'{contador} - {soma}')


