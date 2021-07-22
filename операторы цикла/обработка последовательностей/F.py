n = int(input())
last = n
count = 0
while n != 0:
    n = int(input())
    if n > last:
        count += 1
    last = n
print(count)