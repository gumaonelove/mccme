A = [int(x) for x in input().split()]
B = [0]*len(A)
if len(A)%2==0:
    for i in range(0, len(A), 2):
        B[i], B[i+1] = A[i+1], A[i]
else:
    for i in range(0, len(A)-1, 2):
        B[i], B[i+1] = A[i+1], A[i]
    B[-1]=A[-1]
print(*B)