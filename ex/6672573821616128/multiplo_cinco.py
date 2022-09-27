def multiplo(lim):
    aux = lim-1
    for num in range(1, lim):
        if num > 5 and num % 5 == 0 and num % 2 == 0:
            print(num)
            
lim = int(input())
multiplo(lim)
