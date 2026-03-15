from math import inf

n, l, r, x = list(map(int, input().split()))
resp = 0
v = list()

for i in range(n):
    v.append(int(input()))

for mask in range(0, (1 << n)): # Percorrer todas as combinações de provas possíveis
    soma = 0
    maior = 0
    menor = inf

    for i in range(n): # Percorre todos os bits

        if mask & (1 << i): # verificar se essa questão está na prova:

            soma += v[i]
            maior = max(maior, v[i])
            menor = min(menor, v[i])
    
    if soma >= l and soma <= r and (maior - menor) <= x:
        resp+=1


print(resp)