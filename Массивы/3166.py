A = [int(x) for x in input().split()]
last = A[-1]
B = [0]*len(A)
for i in range(0, len(A)-1, 1):
    B[i+1]=A[i]
else:
    B[0]=last
print(*B)