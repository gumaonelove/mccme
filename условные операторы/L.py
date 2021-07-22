n = int(input())
m = int(input())
k = int(input())

if ((n*m-k)%n==0 or (n*m-k)%m==0) and m*n>k:
    print("YES")
else:
    print("NO")