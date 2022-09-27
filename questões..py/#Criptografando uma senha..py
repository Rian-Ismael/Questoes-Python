#Criptografando uma senha.
#Matrícula: 121210197
#Nome: Rian Ismael Elias de Melo.

# substituição das letras de uma palavra por números considerando o seguinte mapeamento:

# A letra a é substituída pelo número 4.
# A letra e é substituída pelo número 3.
# A letra i é substituída pelo número 1.
# A letra o é substituída pelo número 0.




senha = input()
senha = list(senha)
troca = 0
for i in range(len(senha)):
    if senha[i].lower() == "a":
        senha[i] = '4'



criptografia = "".join(senha)
print(criptografia)        
    