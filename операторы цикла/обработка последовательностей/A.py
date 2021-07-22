n = int(input())
if n == 0:
    count = 0
else:
    count = 1
while n != 0:
    n = int(input())
    if n != 0:
        count += 1
print(count)