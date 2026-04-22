
a, b = map(int, input().split())


qtdA = 0
qtdB = 0

a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])


for elemento in a:
    if elemento not in b:
        qtdA += 1
        
for elemento in b:
    if elemento not in a:
        qtdB += 1       

print(min(qtdA, qtdB))