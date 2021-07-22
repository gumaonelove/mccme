a = int(input())
F = [0, 1]
def fib1(n):
    if n >= 2:
        for i in range(2, n+1):
            F.append(F[i-2] + F[i-1])
fib1(a*2)
try:
    print(F.index(a))
except:
    print(-1)
