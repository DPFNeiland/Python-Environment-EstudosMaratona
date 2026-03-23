n = int(input())

qtd = {}

for _ in range(n):
    aux = int(input())
    
    if aux in qtd.keys():
        qtd[aux] += 1

    else:
        qtd[aux] = 1

aux = sorted(qtd)

for valor in aux:
    print(f"{valor} aparece {qtd[valor]} vez(es)")