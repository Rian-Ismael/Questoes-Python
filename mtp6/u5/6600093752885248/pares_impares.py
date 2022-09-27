pares = 0
impares = 0

while (True):
	entrada = input()
	if (entrada == "fim"): break
	entrada = int(entrada)
	if (entrada % 2 == 0): pares += 1
	elif (entrada % 2 != 0): impares += 1

if pares != 0:
	print(f"pares = {pares}")
if impares != 0:
    print(f"ímpares = {impares}")
