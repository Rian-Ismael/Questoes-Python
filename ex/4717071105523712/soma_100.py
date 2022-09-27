num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= 0 and num2 >= 0 and num3 >= 0:
    soma = num1+num2+num3
    if soma == 100:
        print("*")
    else:
        print(soma)

elif num1 >= 0 and num2 >= 0 and num3 < 0:
    soma = num1+num2
    if soma == 100:
        print("*")
    else:
        print(soma)

elif num1 >= 0 and num2 < 0:
    soma = num1
    if soma == 100:
        print("*")
    else:
        print(soma)

else:
    print(0)

