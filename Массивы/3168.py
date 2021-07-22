A = [int(x) for x in input().split()]
X = int(input())
A.pop(X)
print(*A)