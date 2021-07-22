n = int(input())
suma = 0
while n != 0:
    if n % 10 == 0:
        suma += 1
    n = n // 10

print(suma)