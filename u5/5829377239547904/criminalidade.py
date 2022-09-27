media_mensal_secre = float(input())

nova = []
while True:
    ocorrencia_diaria = input()
    if ocorrencia_diaria == "fim":
        for elemento in nova:
            print(elemento)
        break

    ocorrencia_separada = ocorrencia_diaria.split()

    soma = 0
    for ocorrencia in range(len(ocorrencia_separada)):
        soma += int(ocorrencia_separada[ocorrencia])

    media = float(soma/len(ocorrencia_separada))

    if media > media_mensal_secre:
        nova.append(ocorrencia_diaria)

    if media < (media_mensal_secre/2):
        for elemento in nova:
            print(elemento)
        break
