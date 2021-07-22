a = int(input())
b = int(input())
c = int(input())

if a > b :
    M = a
    N = b
else:
    M = b
    N = a
if c > M:
    print(N, M, c)
elif c < N:
    print(c, N, M)
else:
    print(N, c, M)