n = int(input())
if n == 0:
    summa = 0
else:
    summa = n
while n != 0:
    n = int(input())
    if n != 0:
        summa += n
print(summa)