'''
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько
в нем различных элементов.
'''
A = [int(x) for x in input().split()]
count  = 1
last = A[0]
A.pop(0)
for a in A:
    if a!=last: count += 1
    last = a
print(count)