n, m = map(int, input().split())
count = 1
while m > n:
    if m % n == 0:
        count = 0
    count += m // n
    m -= (n * count + m % n)
print(count)