

def reverse(string: str):

    resp = ""

    q = len(string)
    for i in range(q - 1, -1, -1):
        resp += string[i]

    return resp

while True:
    try:
        a, b = map(int, input().split())

        a: str = bin(a)
        b: str = bin(b)

        resp = ""


        a = reverse(a[2:len(a)])
        b = reverse(b[2:len(b)])

        n = min(len(a), len(b))


        if len(a) > len(b):
            for i in range(n, len(a)):
                b += "0"

        elif len(a) < len(b):
            for i in range(n, len(b)):
                a += "0"
                
        a = reverse(a)
        b = reverse(b)

        n = max(len(a), len(b))


        for i in range(0,n):
            aux = n - i
            
            if a[i] == "0" and b[i] == "0":
                resp+="0"
            
            elif a[i] == "0" and b[i] == "1":
                resp+="1"

            elif a[i] == "1" and b[i] == "0":
                resp+="1"

            elif a[i] == "1" and b[i] == "1":
                resp+="0"
        
        soma = 0
        for i in range(len(resp)):
            soma += int(resp[i])*2**(n-i-1)

        print(soma)

    except EOFError:
        break