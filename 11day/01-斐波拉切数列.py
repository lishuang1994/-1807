def fib():
    a,b = 0,1
    for i in range (10):
        yield b
        a,b = b,a+b
G = fib()
#print(next(G))
for i in G:
    print(i)
