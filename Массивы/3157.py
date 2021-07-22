a = [int(x) for x in input().split()]
b = len(a)
c = 0
for i in range(1, b-1):
    if a[i-1] < a[i] > a[i+1]: c += 1
print(c)