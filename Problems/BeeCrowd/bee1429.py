
fatorial = [1, 2, 6, 24, 120]

n = str(input())

while n != "0":
    soma = 0
    for i in range(len(n)):
        soma += int(n[i])*fatorial[len(n)-i-1]

    print(soma)
    n = str(input())
