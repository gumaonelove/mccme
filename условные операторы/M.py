k = int(input())

if k==1 or k==4:
    print("YES")

else:
    if k%4==0 and k>4:
        a = k/4
        delta = (a-1)**2
        vsego = (a+1)**2
        if vsego-k==delta:
            print("YES")

    else:
        print("NO")