A = [int(x) for x in input().split()]
A.append(A[-1])
ind, num = map(int, input().split())
B = [0]*(len(A))
for i in range(0, len(A), 1):
    if i == ind:
        B[i]=num
        #print(A[i], B[i],1)
    elif i < ind:
        B[i]=A[i]
        #print(A[i], B[i],2)
    else:
        B[i] = A[i-1]
        #print(A[i], B[i],3)
print(*B)