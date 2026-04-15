from math import pow

def fib(n, m):
    
    inicial = [
                [1,1],
                [1,0]
            ]
    
    for i in range(n):
        inicial[0]                
    
    return inicial[0][1]
    
while True:
    n, m  = map(int, (input().split()))
    print(fib(fib(n, m),m))