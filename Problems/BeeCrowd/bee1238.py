

n = int(input())

for _ in range(n):

    stringA, stringB = input().split()

    n = min(len(stringA), len(stringB))
    resp = ""
    for i in range(n):
        resp+= stringA[i] +  stringB[i]

    if len(stringA) > len(stringB):
        aux = len(stringA)
        for i in range(n, len(stringA)):
            resp += stringA[i]

    
    if len(stringA) < len(stringB):
        aux = len(stringB)
        for i in range(n, len(stringB)):
            resp += stringB[i]

    print(resp)