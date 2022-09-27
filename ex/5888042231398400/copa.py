import math
figurinhas_album = int(input())
figurinhas_pacote = int(input())
nao_repetidas = float(input())
preco_pacote = float(input())

numero_pacotes = math.ceil(figurinhas_album / nao_repetidas)
#quantidade de pacotes

preco_total = numero_pacotes * preco_pacote

numero_repetidas = int(numero_pacotes * (figurinhas_pacote - nao_repetidas))

print(f'{numero_pacotes}\n{numero_repetidas}\nR${preco_total:.2f}')    
