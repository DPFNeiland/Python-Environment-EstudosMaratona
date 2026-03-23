

n = int(input())
primeiro = True

while n != 0:
    strings = []
    width = -1
    
    for _ in range(n):  
        aux = str(input())

        aux = " ".join(aux.split())
        strings.append(aux)

        if len(aux) > width:
            width = len(aux)

    if not primeiro:
        print()
    primeiro = False

    for i in range(n):
        print(f"{strings[i]:>{width}}")

    n = int(input())
    