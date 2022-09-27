#Reprovados por falta
#Matrícula: 121210197

#Faltas > 8 --> reprovado

def mycount(sequencia):
    i = 0
    cont = 0
    while i < len(sequencia):
        if sequencia[i] == "f":
            cont += 1
        i += 1
    return cont

reprovados = 0
while True:
    registro = input()

    if registro == "-":
        break

    else:
        if mycount(registro) > 8:
            reprovados += 1

print(f"{reprovados} aluno(s) reprovado(s) por falta.")
