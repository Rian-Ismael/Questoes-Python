#Acima da média (Criminilidade)
# ele deseja selecionar os meses em que a média 
# de ocorrências por dia for maior que a média 
# estabelecida pela secretaria de segurança pública 
# (ssp).

##Seu programa deve imprimir na saída apenas 
# as sequências cuja média mensal é maior 
# que o estabelecido.

#o programa também deve parar de ler 
#a entrada quando receber uma sequência de 
#valores cuja média seja 2 vezes menor que o 
#valor limite indicado na primeira linha da entrada.

#saida: apenas a sequencia que a media mensal é maior que a estabelecida
#Ou a palavra "fim" ou quando a média da sequencia é 2 vezes menor que a estabelecida pela ssp

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