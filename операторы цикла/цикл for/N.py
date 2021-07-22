n = int(input())
count_0 = 0
count_ot = 0
count_pol = 0
for i in range (0, n):
    b = int(input())
    if b == 0:
        count_0 += 1
    elif b > 0:
        count_pol += 1
    else:
        count_ot += 1

print(count_0, count_pol, count_ot)