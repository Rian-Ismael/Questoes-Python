nome1 = input()
nome2 = input()
nome3 = input()

ordem_alfabetica = [nome1[0], nome2[0], nome3[0]]


if ordem_alfabetica[0] < ordem_alfabetica[1] and ordem_alfabetica[0] < ordem_alfabetica[2]:
    print(f"{nome1} (1)")

elif ordem_alfabetica[1] < ordem_alfabetica[0] and ordem_alfabetica[1] < ordem_alfabetica[2]:
    print(f"{nome2} (1)")

elif ordem_alfabetica[2] < ordem_alfabetica[0] and ordem_alfabetica[2] < ordem_alfabetica[1]:
    print(f"{nome3} (1)")

else:

    if nome3[0] == nome1[0]:
        print(f"{nome1} (2)")

    elif nome2[0] == nome3[0]:
        print(f"{nome2} (2)")

    else:
        print(f"{nome1} (2)")

