n = int(input())
if n == 0:
    M = 0
else:
    M = n
N = 0
while n != 0:
    n = int(input())
    if n > M:
        N = M
        M = n
    elif n > N:
        N = n

print(N)