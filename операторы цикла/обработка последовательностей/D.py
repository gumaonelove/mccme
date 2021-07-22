n = int(input())
if n % 2 == 0:
    count = 1
else:
    count = 0

while n != 0:
    n = int(input())
    if n != 0 and n % 2 == 0:
        count += 1
print(count)