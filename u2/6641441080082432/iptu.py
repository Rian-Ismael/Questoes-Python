# IPTU
# uma alíquota que determina o valor por metro quadrado da região
#IPTU = (area_construida * aliquota) + 35(limpeza)
# 1x = 25%IPTU
# 6x = 5%IPTU
# 10x = IPTU


area_construida = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

iptu = (area_construida * aliquota) + 35
valor = iptu
print(f"IPTU: R$ {valor:.2f}\n")

uma_parcela = (iptu - (iptu*(25/100) ))

seis_parcelas = (iptu - (iptu*5/100))
cada_seis_parcelas = (seis_parcelas / 6)

dez_parcelas = iptu
cada_dez_parcelas = iptu/10

print("Pagamento:")
print(f"1. Quota única. R$ {uma_parcela:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {seis_parcelas:.2f}\n   6 x R$ {cada_seis_parcelas:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {dez_parcelas:.2f}\n   10 x R$ {cada_dez_parcelas:.2f}")
