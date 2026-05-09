resp = -1
a = int(input())
b = int(input())
c = int(input())


if a == b:
    resp = c
    
elif a == c:
    resp = b

else:
    resp = a
    
print(resp)