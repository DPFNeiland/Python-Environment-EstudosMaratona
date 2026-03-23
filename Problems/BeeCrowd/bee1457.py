
def kfatorial(n: int, k: int):

    if n <= 1:
        return 1
    
    return n*kfatorial(n-k,k)

qtd = int(input())

for _ in range(qtd):
    instacia = input()
    
    i = 0
    aux = instacia[i]
    n = ""
    while aux.isdigit():
        n += aux
        i += 1
        aux = instacia[i]

    n = int(n)
    k = instacia.count("!")

    print(kfatorial(n, k))