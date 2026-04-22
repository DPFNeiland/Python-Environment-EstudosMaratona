def fib(n, m):
    if n == 0:
        return (0, 1)

    a, b = fib(n // 2, m)

    c = (a * ((2 * b - a) % m)) % m
    d = (a * a + b * b) % m

    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % m)
    
while True:
    
    try:
        n, m  = map(int, (input().split()))
        print(fib(fib(n, m)[0],m)[0])
    except EOFError:
        break
    