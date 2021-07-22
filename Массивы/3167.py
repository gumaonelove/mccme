A = [int(x) for x in input().split()]
maxi = max(A)
mini = min(A)
B = [0]*len(A)
for i in range(0, len(A), 1):
    if A[i] == maxi: B[i] = mini
    elif A[i] == mini: B[i] = maxi
    else: B[i] = A[i]

print(*B)
