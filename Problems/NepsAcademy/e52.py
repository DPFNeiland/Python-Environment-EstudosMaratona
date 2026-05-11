

a = False
b = False

n = int(input())

interruptores = list(map(int, input().split()))

for interruptor in interruptores:
    if interruptor == 1:
        a = not a
    
    if interruptor == 2:
        a = not a
        b = not b

print(int(a))
print(int(b))