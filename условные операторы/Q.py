k = int(input())

while k > 0:
    if k % 3 == 0:
        k -= 3
    elif k % 5 == 0:
        k -= 5
    elif (k-3) % 5 == 0:
        k -= 5
    elif (k-5) % 3 == 3:
        k -= 3
    else:
        k -= 3

else:
    if k == 0:
        print("YES")
    else:
        print("NO")