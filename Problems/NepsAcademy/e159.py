
soma = 0
x = 0

n = int(input())

valores =  list(map(int, (input().split())))

for x in valores:
    soma += x

print(soma)