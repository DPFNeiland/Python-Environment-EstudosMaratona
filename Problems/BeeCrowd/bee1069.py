



n = int(input())


for _ in range(n):
    teste = input()

    pilha = []
    resp = 0

    for valor in teste:
        if valor == "<" or valor == ">":
            
            qtd = len(pilha)

            if valor == "<":
                pilha.append("<")
            
            elif valor == ">" and qtd > 0:
                pilha.pop()
                resp += 1

    print(resp)