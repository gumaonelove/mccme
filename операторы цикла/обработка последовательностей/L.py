n = int(input())

if n == 0:
    count = 0
else:
    count = 1

last = n
M = 1
count = 1

while n != 0:
    n = int(input())

    if n != last:
        count += 1

    elif count > M:
        M = count
        count = 1

    last = n

print(M)