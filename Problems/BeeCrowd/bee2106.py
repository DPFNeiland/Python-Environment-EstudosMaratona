from math import inf
n = 1

while n != 0: 
    preco = list()
    resp = 0
    n = int(input())

    for i in range(n):
        preco.append(list(map(int, input().split())))

    for mask in range(0, 1 << n): # eu vejo todas as possibilidades
        for i in range(n): # percorrer cada jogador
            
            if (mask & (1 << i)):
                soma += preco[i]


    print(resp)