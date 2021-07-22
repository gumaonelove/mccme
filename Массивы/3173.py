A = [int(x) for x in input().split()]
B = {} # {id: count}
for a in A:
    if B.get(a)!=None: B[a]+=1
    else: B[a]=1
maxi_count = 0
maxi_value = 0
for b in B:
    if B[b]> maxi_count:
        maxi_value = b
        maxi_count = B[b]
print(maxi_value)
