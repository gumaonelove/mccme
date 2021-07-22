A = [int(x) for x in input().split()]
B = []
for i in range(len(A)):
    B.append(A[len(A)-i-1])
print(*B)