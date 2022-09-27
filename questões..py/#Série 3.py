#Divisores próprios
# x > 0
# x / y(y<x)

num = int(input())

for n in range(1, num):
    if num % n == 0:   
        print(n)