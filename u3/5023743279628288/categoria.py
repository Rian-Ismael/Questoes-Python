def categoria_idade(nome, idade, categoria):
    mensagem = f"{nome}, {idade} anos, {categoria}."
    return mensagem

nome = input()
idade = int(input())

if idade < 5:
    categoria = "Não pode competir"

elif idade <= 7:
    categoria = "Infantil A"

elif idade <= 10:
    categoria = "Infantil B"

elif idade <= 13:
    categoria = "Juvenil A"

elif idade <= 17:
    categoria = "Juvenil B"

else:
    categoria = "Senior"


categoria_final = categoria_idade(nome, idade, categoria)
print(categoria_final)





