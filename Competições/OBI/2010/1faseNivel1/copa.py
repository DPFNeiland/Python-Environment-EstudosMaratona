
from collections import deque

resultados = list()
quartas = deque()
semi = deque()
final = deque()


jogadores = deque(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"])

      
      
for _ in range(15):
    resultados.append(input().split())
    
# Calculo das oitavas

for i in range(8):
    if int(resultados[i][0]) > int(resultados[i][1]):
        quartas.append(jogadores.popleft())
        jogadores.popleft()
        
    else:
        jogadores.popleft()
        quartas.append(jogadores.popleft())
        
        
# Calculo das quartas
for i in range(8, 12):        
    if int(resultados[i][0]) > int(resultados[i][1]):
        semi.append(quartas.popleft())
        quartas.popleft()
        
    else:
        quartas.popleft()
        semi.append(quartas.popleft())
        
# Calculo da semi
for i in range(12, 14):        
    if int(resultados[i][0]) > int(resultados[i][1]):
        final.append(semi.popleft())
        semi.popleft()
        
    else:
        semi.popleft()
        final.append(semi.popleft())
        
# Calculo da final

if int(resultados[14][0]) > int(resultados[14][1]):
    print(final.popleft())
    
else:
    final.popleft()
    print(final.popleft())
    