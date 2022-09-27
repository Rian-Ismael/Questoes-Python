#Criptografando uma Senha
#Matrícula: 121210197

# A letra a é substituída pelo número 4.
# A letra e é substituída pelo número 3.
# A letra i é substituída pelo número 1.
# A letra o é substituída pelo número 0.

senha = input()
senha = list(senha)
trocas = 0
for num in range(1, len(senha)):
    if senha[num].lower() == "a":
        senha[num] = "4"
        trocas += 1
    if senha[num].lower() == "e":
        senha[num] = "3"
        trocas += 1
    if senha[num].lower() == "i":
        senha[num] = "1"
        trocas += 1
    if senha[num].lower() == "o":
        senha[num] = "0"
        trocas += 1


for letra in senha:
    print(letra, end='')

print(f" ({trocas} troca(s))")
