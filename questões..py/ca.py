# Organiza por último dígito
# Um banco utiliza um critério próprio para organizar os seus clientes na fila de espera. Dada uma fila de chegada, a regra privilegia os clientes cujo último dígito do número da conta for menor ou igual a 5. Assim, esses clientes devem ser atendidos antes dos clientes que não atingem o critério do último dígito.

# Naturalmente, se houver mais de um cliente cujo último digito do número da conta é menor ou igual a 5, esses clientes devem ser atendidos por ordem de chegada entre eles.

# Ainda, os clientes que não atingirem o critério, devem ser atendidos depois dos privilegiados, por ordem de chegada.

# Implemente a função privilegia_digito(fila) que, dada uma lista com o número das contas dos clientes na ordem de chegada, altere a lista aplicando a regra definida acima.

# Exemplo de uso da função
# lista = [19, 18, 13, 1, 2, 16]
# assert privilegia_digito(lista) == None
# assert lista == [13, 1, 2, 19, 18, 16]
# Note que os clientes com último dígito menor ou igual a 5 foram acomodados no início da fila (por ordem de chegada entre eles). Além disso, os clientes com último dígito maior que 5 ocupam as últimas posições da lista (por ordem de chegada entre eles).

# Funções que não devem ser utilizadas
# - insert
# - pop
# - remove
# - sort


def privilegia_digito(lista):
    nova_lista = []
    maior = []
    for i in range(len(lista)):
        lista[i] = str(lista[i])
        if len(lista[i]) >= 2:
            if lista[i][len(lista[i])] <= 5:
                nova_lista.append(lista[i])
            else:
                maior.append(lista[i])

        elif len(lista[i]) < 2:
            if lista[i] <= 5:
                nova_lista.append(lista[i])
            else:
                maior.append(lista[i])
            
    return nova_lista+maior


lista = [19, 18, 13, 1, 2, 16]
print(privilegia_digito(lista))
# assert lista == [13, 1, 2, 19, 18, 16]