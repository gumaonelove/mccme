A = int(input())
B = int(input())

while A != B:
    if A % 2 == 0 and A >= 2 * B:
        A /= 2
        print(':2')
    elif A - 1 >= B:
        A -= 1
        print('-1')