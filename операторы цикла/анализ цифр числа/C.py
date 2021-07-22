n = int(input())
maxim = n % 10
minim = n % 10
while n != 0:
    m = n % 10
    if m >= maxim:
        maxim = m
    elif m <= minim:
        minim = m
    n = n // 10

print(minim, maxim)