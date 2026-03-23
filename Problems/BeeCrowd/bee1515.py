from math import inf

n = int(input())

while n != 0:

    planetaResp = ""
    planetaAnoMenor = inf
    for _ in range(n):        
        mensagem = input()
        planeta, ano, qtdanos = mensagem.split()

        if planetaAnoMenor > (int(ano) - int(qtdanos)):
            planetaAnoMenor = int(ano) - int(qtdanos)
            planetaResp = planeta

    print(planetaResp)

    n = int(input())
