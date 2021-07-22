n = int(input())
A = [[0], [0]]
ok = True
for i in range(n): A[i] = [int(x) for x in input().split()]
for i in range(n):
    for j in range(i+1, n):
        now = A[i][j]
    if i == 0:
        pass