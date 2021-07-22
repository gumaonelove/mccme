n = int(input())
#A=[[0],[0]]*n
for i in range(n):
    for j in range(n):
        if i < n-j-1:
            print(0, end=' ')
        elif i == n-j-1:
            print(1, end=' ')
        else: print(2, end=' ')
    print('')