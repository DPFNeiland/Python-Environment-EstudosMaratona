

def calculo_quadrado_magico(lista):
    aux = 0
    soma = 0
    
    for i in range(len(lista)):
        soma += lista[0][i]        
        
        
    # verificação das somas das linhas

    for i in range(len(lista)):
        for j in range(len(lista)):
            aux += lista[i][j]
        if aux != soma:
            return -1
        
        aux = 0
        
    # verificação das soma das colunas
    for i in range(len(lista)):
        for j in range(len(lista)):
            aux += lista[j][i]
        
        if aux != soma:
            return -1
        
        aux = 0
    # verificação da diagonal principal
    
    for i in range(len(lista)):
        aux += lista[i][i]

    if aux != soma:
        return -1
    
    aux = 0
    
    
    # verificação da diagonal secundário
    for i in range(len(lista)):
        aux += lista[i][len(lista)-i-1]
        
    if aux != soma:
        return -1
    
    aux = 0
    
    
    return soma            
def main():
    n = int(input())
    lista = list()


    for _ in range(n):
        lista.append(list(map(int, input().split())))
        
        
    # cálculo do quadrado
    print(calculo_quadrado_magico(lista))


if __name__ == "__main__":
    main()