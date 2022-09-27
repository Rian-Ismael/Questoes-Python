palavras_lidas = 0
while True:
    palavra = input().lower()
    consoantes = 0
    vogais = 0
    for letra in palavra:
        if letra in "aeiou":    
            vogais += 1
        if letra in "bcdfghijklmnpqrstvxwyz":
            consoantes += 1 

    palavras_lidas += 1

    if consoantes > vogais: break
print(palavras_lidas)
