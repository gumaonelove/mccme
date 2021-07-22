n = int(input())
if n == 0:
    count = 0
    summa = 0
else:
    count = 1
    summa = n
while n != 0:
    n = int(input())
    if n != 0:
        count += 1
        summa += n
print(summa/count)

