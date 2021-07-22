A = [int(x) for x in input().split()]
B = []
for i in range(len(A)-1, -1, -1):
    B.append(A[i])

print(*B)