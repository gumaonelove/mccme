A = [int(x) for x in input().split()]
l = len(A)
n = A.count(0)
for i in range(n): A.remove(0)
A[l-n:]=[0]*(n)
print(*A)