A = [int(x) for x in input().split()]
B = {} # {id: count}
for a in A:
    if B.get(a)!=None: B[a]+=1
    else: B[a]=1
for b in B:
    if B[b]==1: print(b, end = ' ')