A = [int(x) for x in input().split()]
P = int(input())
A.append(0)
A.sort(reverse=True)
#print(A)
for i in range(len(A)):
    if P>A[i]:
        print(i+1)
        break
