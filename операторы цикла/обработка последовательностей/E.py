n = int(input())
if n == 0:
    M = 0
else:
    M = n
while n != 0:
    n = int(input())
    if n > M:
        M = n
print(M)