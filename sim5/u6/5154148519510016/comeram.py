def quantos_comeram(n, fila_pedidos):
    quantia_disponivel = n
    quantia_vendida = 0
    for pedido in fila_pedidos:
        if quantia_disponivel >= pedido:
            quantia_disponivel -= pedido
            quantia_vendida += pedido
        else:
            return quantia_vendida
    return quantia_vendida    
