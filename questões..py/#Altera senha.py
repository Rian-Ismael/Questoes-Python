#Altera senha

senha_atual = input()
senha_nova = input()
#senha_atual: abelha --> len: 6; range: 0, 1, 2, 3, 4, 5
#senha_nova: maça --> len: 4;   range: 0, 1, 2, 3
#carac_atual: 0, 1, 2, 3, 4, 5
#carac_novo:  0, 1, 2, 3

igual = False
for carac in range(len(senha_atual)):
    if carac < len(senha_nova):
        if senha_atual[carac] == senha_nova[carac]:
            print(f"'{senha_atual[carac]}' coincidente na posição {carac+1}")
            igual = True

if igual:
    print("Senha não alterada")
else:
    print("Senha alterada")