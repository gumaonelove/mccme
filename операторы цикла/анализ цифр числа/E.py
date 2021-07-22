n = int(input())
res = ''
while n != 0:
    res += str(n % 10)
    n = n // 10
print(res)