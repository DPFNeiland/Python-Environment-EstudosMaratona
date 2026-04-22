from collections import deque

n = int(input())

chaves = deque()
resp = True

for _ in range(n):
    string = input()
    
    for char in string:
        
        if char != "{" or char != "}":
            if char == "{":
                chaves.append(1)
            
            elif char == "}" and len(chaves) > 0:
                chaves.pop()
                
            elif char == "}" and len(chaves) == 0:
                resp = False
                
if len(chaves) != 0:
    resp = False

print(f"{"S" if resp else "N"}")