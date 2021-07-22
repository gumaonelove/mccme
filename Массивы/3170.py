A = [int(x) for x in input().split()]
B = {} # {id: count}
for a in A:
    if B.get(a)!=None: B[a]+=1
    else: B[a]=1
count_pare = 0
for b in B:
    count_pare += ( (B[b]*(B[b]-1)) //2 )
print(count_pare)