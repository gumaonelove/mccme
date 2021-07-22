n = int(input())

if n == 0:
    maxsimum = 0
    count = 0
else:
    maxsimum = 1
    count = 1

last = 0

while n != 0:
    n = int(input())

    if last == n:
        count += 1
    elif count > maxsimum:
        maxsimum = count
        count = 1

    last = n

print(maxsimum)