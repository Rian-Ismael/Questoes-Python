#Binary Coded Decimal
def binary_coded(binary, base):
    return int(binary, base)


def my_in(e, sequencia):
    for carac in sequencia:
        if e == carac:
            return True
    return False

def count(sequencia):
    count = 0
    for i in sequencia:
        count += 1
    return count

bcd_invalido = ["1010", "1011", "1100", "1101", "1110", "1111"]

bcd_final = []
while True:
    binary = input()

    if binary == "fim":
        break

    binary_um = ""
    binary_dois = ""
    for i in range(len(binary)):
        if i <= 3:
            binary_um += (binary[i])
        else:
            binary_dois += (binary[i])

    if count(binary) < 8:
        bcd_final.append("Tente novamente.")

    elif  my_in(binary_um, bcd_invalido) or (my_in(binary_dois, bcd_invalido)):
        bcd_final.append("BCD inválido.")

    else:
        valor1 = binary_coded(binary_um, 2)
        valor2 = binary_coded(binary_dois, 2)

        bcd_final.append(f"{valor1}{valor2}")

for final in bcd_final:
    print(final)
