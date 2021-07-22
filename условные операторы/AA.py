'''
Для клетки с координатами (x, y) в таблице размером M × N выведите координаты ее соседей. Соседними называются клетки, имеющие общую сторону.

Входные данные
Даны натуральные числа M, N, x, y (1 ≤ x ≤ M ≤ 109, 1 ≤ y ≤ N ≤ 109).

Выходные данные
В выходной файл выведите пары координат соседей этой клетки в произвольном порядке.
'''

M, N = map(int, input().split())
x, y = map(int, input().split())

if 1 < x < M and 1 < y < N:
    print(x - 1, y)
    print(x + 1, y)
    print(x, y + 1)
    print(x, y - 1)

elif 1 == x == y and x < M and y < N:
    print(x + 1, y)
    print(x, y + 1)
elif x == M and y == N and M != 1 and N != 1:
    print(x - 1, y)
    print(x, y - 1)
elif x == M != 1 and y < N:
    if y == 1:
        print(x - 1, y)
        print(x, y + 1)
    else:
        print(x - 1, y)
        print(x, y - 1)
        print(x, y + 1)
elif y == N != 1 and x < M:
    if x == 1:
        print(x, y - 1)
        print(x + 1, y)
    else:
        print(x - 1, y)
        print(x, y - 1)
        print(x + 1, y)
elif x == 1 != M and y < N:
    print(x, y + 1)
    print(x, y - 1)
    print(x + 1, y)
elif y == 1 != N and x < M:
    print(x + 1, y)
    print(x - 1, y)
    print(x, y + 1)
elif x == 1 != N:
    if y == 1:
        print(x, y+1)
    elif y == N:
        print(x, y-1)
    else:
        print(x, y + 1)
        print(x, y - 1)
elif y == 1 != M:
    if x == 1:
        print(x + 1, y)
    elif x == M:
        print(x - 1, y)

    else:
        print(x + 1, y)
        print(x - 1, y)