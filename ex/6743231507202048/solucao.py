hectares = int(input())
herdeiros = int(input())

hectares_inteiros = hectares // herdeiros
hectares_doados = hectares % herdeiros


print("Cada herdeiro deverá receber " + str(hectares_inteiros) + " " + "hectare(s).")
print(str(hectares_doados) + " " + "hectare(s) para doação.")


