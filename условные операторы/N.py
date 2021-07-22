a=int(input())
b=int(input())
if a!=0:
    x = (-b)/a
    if float(x) == float(int(x)):
        print(int(x))
    else:
        print("NO")
else:
    if b == 0:
        print("INF")
    else:
        print("NO")

