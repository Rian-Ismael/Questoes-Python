#Rian Ismael Elias de Melo
#Matrícula: 121210197
#Questão: Altera Senha
#rian.melo@ccc.ufcg.edu.br

senha_antiga = input()
senha_nova = input()

tem_caractere_coincidente = False
for i in range(len(senha_antiga)):
    if (i < len(senha_nova)):
        if (senha_antiga[i] == senha_nova[i]):
            print(f"'{senha_antiga[i]}' coincidente na posição {i+1}")
            tem_caractere_coincidente = True

if tem_caractere_coincidente or len(senha_nova) == 0:
    print("Senha não alterada")
else:
    print("Senha alterada com sucesso")
