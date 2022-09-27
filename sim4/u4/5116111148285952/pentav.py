entrada = input()
saida = 0
for palavra in entrada.split(" "):
    a,e,i,o,u = False,False,False,False,False
    for letra in palavra:
          if letra == "a":
               a = True
          elif letra == "e":
               e = True
          elif letra == "i":
              i = True
          elif letra == "o":
              o = True
          elif letra == "u":
              u = True

    if a and e and i and o and u:
        saida += 1

print(f"Quantidade de pentavogalicas: {saida}")
