n = int(input())
count = 1
M = n
while n != 0:
    n = int(input())
    if n > M:
        M = n
        count = 0
    if n == M:
        count += 1


print(count)