while True:
    a = int(input("a? "))
    b = int(input("b? "))
    c = int(input("c? "))
    delta = (b**2) - 4*a*c
    print(delta)
    if delta <= 0: 
        print("equação inválida: tente novamente")
    else:
        raiz1 = ((-b) + (delta**(1/2))) / (2*a)
        raiz2 = ((-b) - (delta**(1/2))) / (2*a)
        print(f"{raiz1:.3f}\n{raiz2:.3f}")
        break

