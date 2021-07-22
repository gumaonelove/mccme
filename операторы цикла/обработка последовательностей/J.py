n = int(input())
last = n
if n == 0:
    summa = 0
else:
    summa = n
while True:
    n = int(input())
    if n != 0:
        summa += n
    if n == 0 and last ==0:
        break
    last = n
print(summa)