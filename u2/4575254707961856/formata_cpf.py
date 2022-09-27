cpf1 = int((input()))
cpf2 = int((input()))
cpf3 = int((input()))

cpf1_str = f"{cpf1}"
cpf2_str = f"{cpf2}"
cpf3_str = f"{cpf3}"

ultimo_cpf1 = int(cpf1_str[len(cpf1_str)-1])
penultimo_cpf1 = int(cpf1_str[len(cpf1_str)-2])
soma_cpf1 = penultimo_cpf1 + ultimo_cpf1
ultimos_cpf1 = cpf1_str[len(cpf1_str)-2]+cpf1_str[len(cpf1_str)-1]

nove_cpf1 = cpf1_str[0]+cpf1_str[1]+cpf1_str[2]+cpf1_str[3]+cpf1_str[4]+cpf1_str[5]+cpf1_str[6]+cpf1_str[7]+cpf1_str[8]
print(f"{nove_cpf1}-{ultimos_cpf1}")
print(soma_cpf1)

ultimo_cpf2 = int(cpf2_str[len(cpf2_str)-1])
penultimo_cpf2 = int(cpf2_str[len(cpf2_str)-2])
soma_cpf2 = penultimo_cpf2 + ultimo_cpf2
ultimos_cpf2 = cpf2_str[len(cpf2_str)-2]+cpf2_str[len(cpf2_str)-1]

nove_cpf2 = cpf2_str[0]+cpf2_str[1]+cpf2_str[2]+cpf2_str[3]+cpf2_str[4]+cpf2_str[5]+cpf2_str[6]+cpf2_str[7]+cpf2_str[8]
print(f"{nove_cpf2}-{ultimos_cpf2}")
print(soma_cpf2)

ultimo_cpf3 = int(cpf3_str[len(cpf3_str)-1])
penultimo_cpf3 = int(cpf3_str[len(cpf3_str)-2])
soma_cpf3 = penultimo_cpf3 + ultimo_cpf3
ultimos_cpf3 = cpf3_str[len(cpf3_str)-2]+cpf3_str[len(cpf3_str)-1]

nove_cpf3 = cpf3_str[0]+cpf3_str[1]+cpf3_str[2]+cpf3_str[3]+cpf3_str[4]+cpf3_str[5]+cpf3_str[6]+cpf3_str[7]+cpf3_str[8]
print(f"{nove_cpf3}-{ultimos_cpf3}")
print(soma_cpf3)
