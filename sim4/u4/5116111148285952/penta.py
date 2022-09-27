def conta(palavra):
    compara = 0
    for letras in range(len(palavra)):
        if palavra[letras] == "a":
            compara += 1
        elif palavra[letras] == "e":
            compara += 1
        elif palavra[letras] == "i":
            compara += 1
        elif palavra[letras] == "o":
            compara += 1
        elif palavra[letras] == "u":
            compara += 1
    return compara


entrada = input().split()

pentav = 0
for palavra in entrada:
    if conta(palavra) == 5:
        pentav += 1



print(f"Quantidade de pentavogalicas: {pentav}")
