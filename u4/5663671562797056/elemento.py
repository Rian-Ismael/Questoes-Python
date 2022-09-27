def busca_elemento(e, lista):
    for i in lista:
        if i == e:
            return 'sim'
    return 'não'

def main():
    n = int(input())
    busca = input().split()
    for i in range(len(busca)):
        busca[i] = int(busca[i])

    print(busca_elemento(n, busca))


if __name__ == "__main__":
    main()

