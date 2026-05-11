
resp = 0
atual = 0

aux = 0
salvo = 0

n = int(input())

v = list(map(int, input().split()))



for i in range(n):
    if i != 0 and v[i] == salvo:
        atual += 1
    
    else:
        atual = 1
        
    salvo = v[i]    
    
        
    if(atual > resp):
        resp = atual
    
    
print(resp)