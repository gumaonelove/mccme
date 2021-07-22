"""
Необходимо вывести одно из слов:
right для прямоугольного треугольника,
acute для остроугольного треугольника,
obtuse для тупоугольного треугольника или
impossible, если входные числа не образуют треугольника.
"""

a = int(input())
b = int(input())
c = int(input())

S = [a,b,c]

M = max(S)
S.remove(M)

N = max(S)
Y = min(S)

#print(M, N, Y)
if a+b<=c or a+c<=b or b+c<=a:
    print("impossible")
elif M == (N**2 + Y**2)**0.5:
    print("right")
elif M**2 < (N**2 + Y**2):
    print("acute")
elif M ** 2 > (N ** 2 + Y ** 2):
    print("obtuse")