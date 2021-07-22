n = int(input())
A = []
for i in range(1, n+1):
    for j in range(1, i+1):
        A.append(i)

print(*A[:n])

