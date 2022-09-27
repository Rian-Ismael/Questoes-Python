soma = 0

while True:
    palavra = input()

    if palavra == 'fim': break
    
    soma += len(palavra)

print(soma)

####################

soma = 0

palavra = input()

while palavra != 'fim':
    soma += len(palavra)

    palavra = input()

print(soma)
