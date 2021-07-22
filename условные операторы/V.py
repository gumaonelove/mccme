a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c

if D < 0:
    pass
if D == 0:
    if int(b) == 0:
        print(0)
    else:
        x1 = (-b) / (2 * a)
        print(x1)
else:
    try:
        x1 = float((-b + D ** 0.5) / (2 * a))
        x2 = float((-b - D ** 0.5) / (2 * a))
        print(x1, x2)
    except:
        pass